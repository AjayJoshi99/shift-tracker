from flask import Flask, render_template, request
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    remaining = None

    IST = timezone(timedelta(hours=5, minutes=30))
    now = datetime.now(IST)

    if request.method == "POST":
        try:
            hours = float(request.form.get("hours") or 0)
            minutes = float(request.form.get("minutes") or 0)

            if hours < 0 or hours > 8:
                error = "Hours must be between 0 and 8"
            elif minutes < 0 or minutes >= 60:
                error = "Minutes must be between 0 and 59"
            elif hours == 8 and minutes > 0:
                error = "Total work cannot exceed 8 hours"
            else:
                worked = (hours * 60) + minutes
                remaining = 480 - worked

                if remaining <= 0:
                    error = "Your shift is already complete 🎉"
                else:
                    end_time = now + timedelta(minutes=remaining)
                    result = end_time.strftime("%I:%M %p")

        except ValueError:
            error = "Invalid input"

    return render_template(
        "index.html",
        result=result,
        error=error,
        remaining=remaining
    )

if __name__ == "__main__":
    app.run()

