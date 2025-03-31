namespace AutoCal.Abstractions;

/// <summary>
///     This interface defines the contract for managing appointments.
///     It includes methods for creating, reading, updating, and deleting appointments.
///     It also includes methods for retrieving appointments by ID and by time range.
///     The implementation of this interface should handle the actual data storage and retrieval.
/// </summary>
public interface IAppointmentManager
{
    /// <summary>
    ///     Creates a new appointment with the specified details.
    /// </summary>
    /// <param name="title"></param>
    /// <param name="startTime"></param>
    /// <param name="endTime"></param>
    /// <param name="location"></param>
    /// <param name="description"></param>
    /// <param name="busyState"></param>
    /// <returns>EventID as string.</returns>
    string CreateAppointment(string title, DateTimeOffset startTime, DateTimeOffset endTime, string location, string description, BusyState busyState);

    // Read an appointment by ID
    Appointment GetAppointment(string id);

    // Update an existing appointment
    void UpdateAppointment(string id, string title, DateTimeOffset startTime, DateTimeOffset endTime, string location, string description, BusyState busyState);

    // Delete an appointment by ID
    void DeleteAppointment(string id);

    // Retrieve a single appointment by ID
    Appointment GetAppointmentById(string id);

    // Retrieve all appointments within a specified time range
    IEnumerable<Appointment> GetAppointments(DateTimeOffset start, DateTimeOffset end);
}


