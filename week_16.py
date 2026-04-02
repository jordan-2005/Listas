import tkinter as tk
from tkinter import messagebox

# ──────────────────────────────────────────────
#  CONFIGURACIÓN VISUAL
# ──────────────────────────────────────────────
BG_MAIN       = "#1e1e2e"
BG_FRAME      = "#2a2a3e"
BG_ENTRY      = "#313145"
BG_BTN_ADD    = "#7c3aed"
BG_BTN_DONE   = "#059669"
BG_BTN_DEL    = "#dc2626"
BG_BTN_HOVER  = "#9d54ff"
FG_WHITE      = "#f1f5f9"
FG_MUTED      = "#94a3b8"
FG_DONE       = "#64748b"
COLOR_DONE_BG = "#1e3a2e"
COLOR_PEND_BG = "#2a2a3e"
FONT_TITLE    = ("Segoe UI", 18, "bold")
FONT_NORMAL   = ("Segoe UI", 11)
FONT_SMALL    = ("Segoe UI", 9)
FONT_BTN      = ("Segoe UI", 10, "bold")


# ──────────────────────────────────────────────
#  CLASE PRINCIPAL
# ──────────────────────────────────────────────
class GestorTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("560x620")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_MAIN)

        # Lista interna: cada elemento es {"texto": str, "completada": bool, "frame": widget, ...}
        self.tareas = []

        self._construir_ui()
        self._registrar_atajos()

    # ── UI ────────────────────────────────────
    def _construir_ui(self):
        # Título
        tk.Label(
            self.root, text="✅ Gestor de Tareas",
            font=FONT_TITLE, bg=BG_MAIN, fg=FG_WHITE
        ).pack(pady=(24, 4))

        tk.Label(
            self.root,
            text="Enter: añadir  •  C: completar  •  D/Supr: eliminar  •  Esc: salir",
            font=FONT_SMALL, bg=BG_MAIN, fg=FG_MUTED
        ).pack(pady=(0, 16))

        # Frame de entrada
        frame_entrada = tk.Frame(self.root, bg=BG_MAIN)
        frame_entrada.pack(padx=24, fill="x")

        self.entry = tk.Entry(
            frame_entrada, font=FONT_NORMAL,
            bg=BG_ENTRY, fg=FG_WHITE, insertbackground=FG_WHITE,
            relief="flat", bd=0
        )
        self.entry.pack(side="left", fill="x", expand=True,
                        ipady=10, ipadx=10)
        self.entry.focus()

        self._btn(frame_entrada, "＋ Añadir", BG_BTN_ADD,
                  self.añadir_tarea).pack(side="left", padx=(10, 0))

        # Frame de botones de acción
        frame_botones = tk.Frame(self.root, bg=BG_MAIN)
        frame_botones.pack(padx=24, pady=10, fill="x")

        self._btn(frame_botones, "✔ Completar [C]", BG_BTN_DONE,
                  self.completar_tarea).pack(side="left", padx=(0, 8))
        self._btn(frame_botones, "🗑 Eliminar [D]", BG_BTN_DEL,
                  self.eliminar_tarea).pack(side="left")

        # Contador
        self.lbl_contador = tk.Label(
            self.root, text="0 tareas",
            font=FONT_SMALL, bg=BG_MAIN, fg=FG_MUTED
        )
        self.lbl_contador.pack(anchor="e", padx=24)

        # Separador
        tk.Frame(self.root, height=1, bg="#3f3f5a").pack(
            fill="x", padx=24, pady=(4, 0))

        # Canvas + scrollbar para la lista
        contenedor = tk.Frame(self.root, bg=BG_MAIN)
        contenedor.pack(padx=24, pady=10, fill="both", expand=True)

        self.canvas = tk.Canvas(contenedor, bg=BG_MAIN,
                                highlightthickness=0)
        scrollbar = tk.Scrollbar(contenedor, orient="vertical",
                                 command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.frame_lista = tk.Frame(self.canvas, bg=BG_MAIN)
        self.canvas_window = self.canvas.create_window(
            (0, 0), window=self.frame_lista, anchor="nw"
        )

        self.frame_lista.bind("<Configure>", self._actualizar_scroll)
        self.canvas.bind("<Configure>", self._ajustar_ancho)
        self.canvas.bind_all("<MouseWheel>", self._scroll_mouse)

        # Mensaje vacío
        self.lbl_vacio = tk.Label(
            self.frame_lista,
            text="No hay tareas. ¡Añade una arriba!",
            font=FONT_NORMAL, bg=BG_MAIN, fg=FG_MUTED
        )
        self.lbl_vacio.pack(pady=40)

    def _btn(self, parent, texto, color, comando):
        b = tk.Button(
            parent, text=texto, font=FONT_BTN,
            bg=color, fg=FG_WHITE, activebackground=color,
            activeforeground=FG_WHITE, relief="flat",
            cursor="hand2", padx=14, pady=8,
            command=comando
        )
        return b

    # ── SCROLL ────────────────────────────────
    def _actualizar_scroll(self, event=None):
        self.canvas.configure(
            scrollregion=self.canvas.bbox("all"))

    def _ajustar_ancho(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def _scroll_mouse(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # ── ATAJOS ────────────────────────────────
    def _registrar_atajos(self):
        self.root.bind("<Return>",  lambda e: self.añadir_tarea())
        self.root.bind("<c>",       lambda e: self.completar_tarea())
        self.root.bind("<C>",       lambda e: self.completar_tarea())
        self.root.bind("<d>",       lambda e: self.eliminar_tarea())
        self.root.bind("<D>",       lambda e: self.eliminar_tarea())
        self.root.bind("<Delete>",  lambda e: self.eliminar_tarea())
        self.root.bind("<Escape>",  lambda e: self._confirmar_salir())

    # ── LÓGICA ────────────────────────────────
    def añadir_tarea(self):
        texto = self.entry.get().strip()
        if not texto:
            self.entry.config(bg="#4a1a1a")
            self.root.after(400, lambda: self.entry.config(bg=BG_ENTRY))
            return

        tarea = {"texto": texto, "completada": False,
                 "frame": None, "lbl": None, "seleccionada": False}
        self.tareas.append(tarea)
        self._renderizar_tarea(tarea)
        self.entry.delete(0, tk.END)
        self._actualizar_contador()

        # Seleccionar la nueva tarea
        self._seleccionar(tarea)

    def _renderizar_tarea(self, tarea):
        if self.lbl_vacio.winfo_ismapped():
            self.lbl_vacio.pack_forget()

        frame = tk.Frame(
            self.frame_lista,
            bg=COLOR_PEND_BG, cursor="hand2"
        )
        frame.pack(fill="x", pady=3, ipady=2)

        # Número de orden
        idx = self.tareas.index(tarea) + 1
        lbl_num = tk.Label(
            frame, text=f"{idx:02d}",
            font=FONT_SMALL, bg=COLOR_PEND_BG, fg=FG_MUTED,
            width=3
        )
        lbl_num.pack(side="left", padx=(10, 4), pady=8)

        # Icono estado
        lbl_icono = tk.Label(
            frame, text="○",
            font=("Segoe UI", 13), bg=COLOR_PEND_BG, fg=FG_MUTED
        )
        lbl_icono.pack(side="left", padx=(0, 8))

        # Texto tarea
        lbl_texto = tk.Label(
            frame, text=tarea["texto"],
            font=FONT_NORMAL, bg=COLOR_PEND_BG, fg=FG_WHITE,
            anchor="w"
        )
        lbl_texto.pack(side="left", fill="x", expand=True)

        tarea["frame"]    = frame
        tarea["lbl"]      = lbl_texto
        tarea["lbl_num"]  = lbl_num
        tarea["lbl_icon"] = lbl_icono

        # Click en cualquier parte del frame = seleccionar
        for widget in (frame, lbl_num, lbl_icono, lbl_texto):
            widget.bind("<Button-1>", lambda e, t=tarea: self._seleccionar(t))

    def _seleccionar(self, tarea):
        # Deseleccionar anterior
        for t in self.tareas:
            if t["seleccionada"] and t is not tarea:
                t["seleccionada"] = False
                self._refrescar_apariencia(t)

        tarea["seleccionada"] = True
        self._refrescar_apariencia(tarea)

    def _refrescar_apariencia(self, tarea):
        if tarea["frame"] is None:
            return

        if tarea["completada"]:
            bg   = COLOR_DONE_BG
            fg   = FG_DONE
            icon = "✔"
            icon_color = "#10b981"
        else:
            bg   = COLOR_PEND_BG
            fg   = FG_WHITE
            icon = "○"
            icon_color = FG_MUTED

        # Borde de selección: borde izquierdo simulado con color de fondo
        sel_bg = "#7c3aed" if tarea["seleccionada"] else bg

        tarea["frame"].config(bg=sel_bg if tarea["seleccionada"] else bg,
                              highlightbackground="#7c3aed" if tarea["seleccionada"] else bg,
                              highlightthickness=2 if tarea["seleccionada"] else 0)

        for w_key in ("lbl", "lbl_num", "lbl_icon"):
            w = tarea.get(w_key)
            if w:
                w.config(bg=sel_bg if tarea["seleccionada"] else bg)

        tarea["lbl"].config(fg=fg,
                            font=("Segoe UI", 11, "overstrike") if tarea["completada"]
                            else FONT_NORMAL)
        tarea["lbl_icon"].config(text=icon, fg=icon_color)

    def completar_tarea(self):
        tarea = self._tarea_seleccionada()
        if not tarea:
            return
        tarea["completada"] = not tarea["completada"]
        self._refrescar_apariencia(tarea)
        self._actualizar_contador()

    def eliminar_tarea(self):
        tarea = self._tarea_seleccionada()
        if not tarea:
            return

        idx = self.tareas.index(tarea)
        tarea["frame"].destroy()
        self.tareas.remove(tarea)

        # Seleccionar la siguiente tarea si existe
        if self.tareas:
            nuevo_idx = min(idx, len(self.tareas) - 1)
            self._seleccionar(self.tareas[nuevo_idx])
        else:
            self.lbl_vacio.pack(pady=40)

        self._renumerar()
        self._actualizar_contador()

    def _tarea_seleccionada(self):
        for t in self.tareas:
            if t["seleccionada"]:
                return t
        return None

    def _renumerar(self):
        for i, t in enumerate(self.tareas):
            if t.get("lbl_num"):
                t["lbl_num"].config(text=f"{i+1:02d}")

    def _actualizar_contador(self):
        total      = len(self.tareas)
        completadas = sum(1 for t in self.tareas if t["completada"])
        self.lbl_contador.config(
            text=f"{total} tarea{'s' if total != 1 else ''}  •  "
                 f"{completadas} completada{'s' if completadas != 1 else ''}"
        )

    def _confirmar_salir(self):
        if messagebox.askokcancel("Salir", "¿Deseas cerrar el Gestor de Tareas?"):
            self.root.destroy()


# ──────────────────────────────────────────────
#  PUNTO DE ENTRADA
# ──────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app  = GestorTareas(root)
    root.mainloop()