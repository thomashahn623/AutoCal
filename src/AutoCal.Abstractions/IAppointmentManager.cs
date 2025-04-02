namespace AutoCal.Abstractions;

public interface IAppointmentManager
{
    string CreateAppointment(string title, DateTimeOffset startTime, DateTimeOffset endTime, string description, BusyState busyState, List<string> categories);
    IAppointment GetAppointment(string id);
    void UpdateAppointment(string id, string title, DateTimeOffset startTime, DateTimeOffset endTime, string location, string description, BusyState busyState, List<string> categories);
    void DeleteAppointment(string id);
    IAppointment GetAppointmentById(string id);
    IEnumerable<IAppointment> GetAppointments(DateTimeOffset start, DateTimeOffset end);
}


