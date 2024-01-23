provider "google" {
  project = "unified-surfer-405214"
  region  = "us-central1"
}


resource "google_storage_bucket" "Homework-Bucket-testingTerra" {
  name          = "unified-surfer-405214-testing_homework"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}