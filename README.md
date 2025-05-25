# JitterByMononoke

![JitterByMononoke Interface](https://via.placeholder.com/400x500.png?text=JitterByMononoke+Interface) *(Placeholder for screenshot)*

## Overview
**JitterByMononoke** is a Python-based tool designed to improve your *Apex Legends* gameplay by counteracting weapon recoil through automated mouse movements. It features a sleek GUI built with `dearpygui` and utilizes `pynput` for precise mouse input detection. Whether you're a competitive gamer or a Python enthusiast, this project offers a robust solution for recoil control and a well-structured codebase for learning and contribution.

## Features
- **Recoil Control**: Automatically moves the mouse to counteract weapon recoil, enhancing shooting accuracy.
- **Customizable Parameters**: Adjust shake strength (`PLUS`/`MINUS`) and delay (`SLEEP_TIME`) via sliders.
- **Mouse Button Flexibility**: Supports multiple activation buttons (e.g., left, right, Mouse4, Mouse5).
- **Responsive GUI**: Built with Dear PyGui, the interface adapts to different screen sizes and resolutions.
- **Efficient Design**: Uses threading for smooth, non-blocking operation with minimal CPU usage.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/JitterByMononoke.git
   ```
2. **Install Dependencies**:
   ```bash
   pip install dearpygui pynput
   ```
3. **Run the Script**:
   ```bash
   python JitterByMononoke.py
   ```

## Usage
1. Launch the application to open the GUI.
2. Adjust the `PLUS`, `MINUS`, and `SLEEP_TIME` sliders to match your weapon's recoil pattern.
3. Select an activation button from the dropdown menu (e.g., Mouse4 or right).
4. Click "Enable" to start the jitter effect. Hold the selected button in-game to activate recoil compensation.
5. Click "Disable" to stop the script.

## Technical Details
- **Language**: Python 3.x
- **Libraries**:
  - `dearpygui`: For the graphical user interface.
  - `pynput`: For mouse input detection and control.
  - `win32api`: For low-level mouse movement simulation (Windows only).
  - `threading`: For non-blocking jitter loop execution.
- **Platform**: Windows (due to `win32api` dependency).
- **Code Structure**:
  - Modular design with clear separation of GUI, input handling, and jitter logic.
  - Dynamic GUI resizing for better usability.
  - Error handling for font and image loading.

## Building an Executable
To create a standalone `.exe` file for easier distribution:
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Run the following command in the project directory:
   ```bash
   pyinstaller --onefile --noconsole JitterByMononoke.py
   ```
3. Find the executable in the `dist` folder.

## Notes
- Ensure you have administrator privileges when running the script, as it interacts with low-level mouse input.
- The script is designed for *Apex Legends* but can be adapted for other games with similar recoil mechanics.
- The background image feature is currently disabled (empty `image_path`). Add a valid image path to enhance the GUI.

## Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please report issues or suggest features via the GitHub Issues page.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Credits
Developed by **rMononoke**. Inspired by the *Apex Legends* community and the need for precise recoil control.

---

# JitterByMononoke (Русская версия)

![Интерфейс JitterByMononoke](https://via.placeholder.com/400x500.png?text=Интерфейс+JitterByMononoke) *(Заглушка для скриншота)*

## Обзор
**JitterByMononoke** — это инструмент на Python, созданный для улучшения игрового процесса в *Apex Legends* за счёт автоматической компенсации отдачи оружия через управление движением мыши. Проект использует `dearpygui` для создания стильного графического интерфейса и `pynput` для точного отслеживания ввода мыши. Это идеальный выбор как для геймеров, так и для разработчиков, интересующихся автоматизацией и GUI.

## Возможности
- **Управление отдачей**: Автоматически корректирует движения мыши для компенсации отдачи, повышая точность стрельбы.
- **Настраиваемые параметры**: Регулировка силы встряски (`PLUS`/`MINUS`) и задержки (`SLEEP_TIME`) через ползунки.
- **Гибкость кнопок мыши**: Поддержка различных кнопок активации (например, левая, правая, Mouse4, Mouse5).
- **Адаптивный интерфейс**: Интерфейс, построенный на Dear PyGui, адаптируется под разные размеры экрана.
- **Эффективность**: Использует потоки для плавной работы с минимальной нагрузкой на процессор.

## Установка
1. **Склонируйте репозиторий**:
   ```bash
   git clone https://github.com/yourusername/JitterByMononoke.git
   ```
2. **Установите зависимости**:
   ```bash
   pip install dearpygui pynput
   ```
3. **Запустите скрипт**:
   ```bash
   python JitterByMononoke.py
   ```

## Использование
1. Запустите приложение, чтобы открыть графический интерфейс.
2. Настройте ползунки `PLUS`, `MINUS` и `SLEEP_TIME` под характеристики отдачи вашего оружия.
3. Выберите кнопку активации в выпадающем меню (например, Mouse4 или правая).
4. Нажмите "Включить", чтобы запустить эффект. Удерживайте выбранную кнопку в игре для компенсации отдачи.
5. Нажмите "Выключить", чтобы остановить скрипт.

## Технические детали
- **Язык**: Python 3.x
- **Библиотеки**:
  - `dearpygui`: Для графического интерфейса.
  - `pynput`: Для обработки ввода мыши.
  - `win32api`: Для низкоуровневого управления мышью (только Windows).
  - `threading`: Для неблокирующего выполнения цикла.
- **Платформа**: Windows (из-за зависимости от `win32api`).
- **Структура кода**:
  - Модульный дизайн с чётким разделением GUI, обработки ввода и логики джиттера.
  - Динамическое изменение размера интерфейса для удобства.
  - Обработка ошибок для загрузки шрифтов и изображений.

## Создание исполняемого файла
Для создания автономного файла `.exe`:
1. Установите PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Выполните команду в директории проекта:
   ```bash
   pyinstaller --onefile --noconsole JitterByMononoke.py
   ```
3. Найдите исполняемый файл в папке `dist`.

## Примечания
- Для работы скрипта могут потребоваться права администратора, так как он взаимодействует с низкоуровневым вводом мыши.
- Скрипт разработан для *Apex Legends*, но может быть адаптирован для других игр с похожей механикой отдачи.
- Функция фонового изображения отключена (пустой `image_path`). Укажите путь к изображению для улучшения интерфейса.

## Вклад в проект
Мы приветствуем любые улучшения! Чтобы внести вклад:
1. Сделайте форк репозитория.
2. Создайте новую ветку (`git checkout -b feature/your-feature`).
3. Зафиксируйте изменения (`git commit -m "Добавлена ваша функция"`).
4. Отправьте ветку (`git push origin feature/your-feature`).
5. Откройте запрос на включение изменений.

Пожалуйста, сообщайте об ошибках или предлагайте новые функции через страницу Issues на GitHub.

## Лицензия
Проект распространяется под лицензией MIT. Подробности смотрите в файле `LICENSE`.

## Автор
Разработано **rMononoke**. Вдохновлено сообществом *Apex Legends* и необходимостью точного контроля отдачи.
