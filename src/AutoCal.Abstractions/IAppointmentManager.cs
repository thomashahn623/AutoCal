namespace AutoCal.Abstractions;

public interface IAppointmentManager
{
    string CreateAppointment(string title, DateTimeOffset startTime, DateTimeOffset endTime, string description, BusyState busyState, List<string> categories);
    Appointment GetAppointment(string id);
    void UpdateAppointment(string id, string title, DateTimeOffset startTime, DateTimeOffset endTime, string location, string description, BusyState busyState, List<string> categories);
    void DeleteAppointment(string id);
    Appointment GetAppointmentById(string id);
    IEnumerable<Appointment> GetAppointments(DateTimeOffset start, DateTimeOffset end);
}


