from meteostat import Hourly, Point
from datetime import datetime
import pandas as pd

# מיקום תל אביב
location = Point(32.0853, 34.7818)

# טווח התאריכים החדש: כל 2024 עד היום
start = datetime(2024, 1, 1)
end = datetime.now()

# שליפת דאטה
data = Hourly(location, start, end)
df = data.fetch()

# עיבוד: איפוס אינדקס + פיצ'רים
df.reset_index(inplace=True)
df['hour'] = df['time'].dt.hour
df['month'] = df['time'].dt.month
df['dayofweek'] = df['time'].dt.dayofweek

# שמירה ל-CSV עם כל העמודות
df.to_csv("tel_aviv_weather_2024_2025.csv", index=False, encoding="utf-8-sig")

# --- ניקוי קל --- #
# טוען את הקובץ מחדש
df = pd.read_csv("tel_aviv_weather_2024_2025.csv")

# הסרת עמודות לא רלוונטיות (למעט wpgt!)
df.drop(columns=["snow", "tsun"], inplace=True)

# הוספת עמודת gust_gap
df["gust_gap"] = df["wpgt"] - df["wspd"]

# הוספת עמודת is_rain
df["is_rain"] = (df["prcp"] > 0).astype(int)

# שמירה לקובץ הסופי
df.to_csv("tel_aviv_weather_cleaned.csv", index=False, encoding="utf-8-sig")

print("✔ נוספו gust_gap ו־is_rain ונשמר בקובץ המעודכן!")
print(df[["wspd", "wpgt", "gust_gap", "prcp", "is_rain"]].head())
print("סה״כ שורות:", len(df))




