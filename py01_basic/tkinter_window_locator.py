import tkinter as tk

class CoordinateTool:
    def __init__(self, root):
        self.root = root

        # 라벨 초기화
        self.label = tk.Label(root, text="마우스로 클릭하세요!")
        self.label.pack(pady=10)

        # 마우스 클릭 이벤트 바인딩
        self.root.bind("<Button-1>", self.on_click)

        # 창 크기 조절 이벤트 바인딩
        self.root.bind("<Configure>", self.on_resize)

    def on_click(self, event):
        # 마우스 클릭 시 호출되는 함수
        click_position_str = f"클릭 위치: {event.x}, {event.y}"
        self.label.config(text=click_position_str)

    def on_resize(self, event):
        # 창 크기 조절 시 호출되는 함수
        window_size_str = f"창 크기: {root.winfo_width()} x {root.winfo_height()}"
        self.root.title(window_size_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = CoordinateTool(root)
    root.geometry("300x200")  # 초기 창 크기
    root.mainloop()