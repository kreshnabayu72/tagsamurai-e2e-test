---
id: TC-GS-ACTLOG-E2E-049-download-gagal-toast-error-dengan-nama-berkas
title: "Download Gagal: Toast Error dengan Nama Berkas"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-132
coverage:
  web: automated
---

# Download Gagal: Toast Error dengan Nama Berkas

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; kelas fault injection, prinsip 13b).
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` (seedSession). Spec tidak mengganti akun.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Data: log Tab Session dan Tab User Action yang sudah ada di environment, hanya dibaca. Spec tidak membuat atau mengubah data.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; endpoint diambil dari openapi dan LLD Activity Log karena TC tidak menyebutnya:
  - `POST /v2/analytics-reporting/session-logs/export` (permintaan export Tab Session, Download as CSV): jawab 500.
  - `POST /v2/analytics-reporting/change-logs/export` (permintaan export Tab User Action, Download as CSV): jawab 500.
- Kemampuan teknis: mengamati toast error beserta teksnya.
- State global yang diubah: intercept respons export (dipasang di langkah 2 dan 7, dilepas di langkah 5 dan 10); hook `after` melepas semua intercept walau spec gagal di tengah.
- Hook `beforeEach`: kembali ke layar Global Settings > Activity Log > Session.

## Test Steps

### TC-GS-ACTLOG-132: Download gagal menampilkan toast error dengan nama berkas, kedua tab

1. Buka Global Settings > Activity Log > Session
2. Pasang intercept pada `POST /v2/analytics-reporting/session-logs/export`: jawab 500
3. Klik icon Download, lalu klik `Download as CSV`
4. Verifikasi muncul toast error: "Error, failed to download Activity-Log-Session."
5. Lepas intercept `POST /v2/analytics-reporting/session-logs/export`
6. Klik tab "User Action"
7. Pasang intercept pada `POST /v2/analytics-reporting/change-logs/export`: jawab 500
8. Klik icon Download, lalu klik `Download as CSV`
9. Verifikasi muncul toast error: "Error, failed to download Activity-Log-User-Action."
10. Lepas intercept `POST /v2/analytics-reporting/change-logs/export`

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`. Mode: FE+BE. Kelas fault injection (prinsip 13b); hanya satu TC, satu kelas.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 5 dan 10 (melepas intercept segera setelah pemicu selesai, S-09), langkah 6 (pindah tab).
- Keterangan "(tanpa ekstensi)" pada Expected TC tercakup oleh teks toast yang diasersi persis (`Activity-Log-Session.` dan `Activity-Log-User-Action.` tanpa `.csv`).
- Pembagian TC lintas spec: unduhan berhasil ada di spec 047 sampai 050; tidak ada TC yang terbelah.
- Temuan untuk QA:
  - TC-GS-ACTLOG-132: Precondition b menyebut "di-intercept" tanpa endpoint; TC tidak menyebut endpoint, sehingga endpoint diambil dari openapi dan LLD (S-13).
  - TC-GS-ACTLOG-132: TC tidak menyebut apakah berkas tidak terunduh saat gagal; tidak diasersi karena bukan Expected.
