provider "google" {
  project = var.project_id
}

resource "google_cloud_run_v2_service" "default" {
  name     = "tf-managed-service"
  location = var.region
  client   = "terraform"

  template {
    containers {
      image = var.image
      ports {
        container_port = 5000
      }
    }
  }
}

resource "google_cloud_run_v2_service_iam_member" "noauth" {
  location = google_cloud_run_v2_service.default.location
  name     = google_cloud_run_v2_service.default.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}