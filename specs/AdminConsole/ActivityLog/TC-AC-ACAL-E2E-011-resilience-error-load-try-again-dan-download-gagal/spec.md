---
id: TC-AC-ACAL-E2E-011-resilience-error-load-try-again-dan-download-gagal
title: "Resilience: Error Load Tabel, Try Again, dan Download Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACAL-09
  - TC-AC-ACAL-10
  - TC-AC-ACAL-131
  - TC-AC-ACAL-132
coverage:
  web: automated
---

# Resilience: Error Load Tabel, Try Again, dan Download Gagal

## Prerequisites

- Mode: mock (seluruh API di-mock; dijalankan tim FE sebagai integration test tanpa backend nyata; resilience menurut bagian 6 konvensi, hanya perilaku FE atas respons mock yang diasersi).
- Aktor yang dimodelkan lewat payload izin mock: Total Control (Principal) (Pre-setup No 1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`. Tidak ada login nyata dan tidak ada password yang dipakai. Seluruh mock dipasang di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite.
- Endpoint yang dipanggil halaman pada kondisi tes dan jawaban mock (path, method, dan skema mengikuti `API/openapi.yaml` dan `API/low-level-design.md` modul; seluruhnya `POST`, prefix `/v2/analytics-reporting`; operasi dengan jawaban 4xx tidak dipakai di spec ini):
  - `POST /v2/analytics-reporting/session-logs/list` (`post_activity_log_session_list`): jawaban normal 200 `{ "message": "Success", "data": { "totalRecords": <integer>, "data": [ActivityLogSessionItem] } }` dengan item berisi `_id`, `createdAt`, `userName`, `employeeId`, `position`, `division`, `activity` (`Session` untuk baris Admin Console), `status`, `note`, `ipAddress`, `deviceBrowser`; sedikitnya 10 baris sehingga tabel dan pagination ter-render (fixture respons mock baru, isi baris ditetapkan tim FE: minimal 10 baris, `totalRecords` konsisten dengan footer). TC-AC-ACAL-09 jawaban 500 `{ "message": "Internal server error" }`; TC-AC-ACAL-10 jawaban 500 pada permintaan pertama lalu 200 normal pada permintaan berikutnya; TC-AC-ACAL-131 dan TC-AC-ACAL-132 jawaban 200 normal.
  - `POST /v2/analytics-reporting/change-logs/list` (`post_activity_log_changelog_list`): jawaban normal 200 dengan `data` berbentuk `{ "totalRecords": <integer>, "data": [ActivityLogChangelogListItem] }`, item berisi `_id`, `createdAt`, `modifiedBy`, `activity`, `object`, `name`, `field`, `oldValue`, `newValue`; sedikitnya 10 baris. Kondisi jawaban 500 per TC sama dengan endpoint Session di atas.
  - `POST /v2/analytics-reporting/session-logs/export` (`post_activity_log_session_export`; body `format` `csv`/`xlsx` dan `fileName`, sukses 200 `application/octet-stream`): TC-AC-ACAL-131 jawaban 500 `{ "message": "Internal server error" }`.
  - `POST /v2/analytics-reporting/change-logs/export` (`post_activity_log_changelog_export`): TC-AC-ACAL-132 jawaban 500 `{ "message": "Internal server error" }`.
  - Stream real-time kedua tab (SSE): tidak ada di `openapi.yaml` maupun `low-level-design.md`; path tidak ditulis (lihat Temuan untuk QA). Koneksi dijawab terbuka tanpa event pada seluruh TC supaya halaman tidak memuat ulang sendiri.
  - `POST /v2/analytics-reporting/session-logs/options` dan `POST /v2/analytics-reporting/change-logs/options` tidak dipanggil pada kondisi tes spec ini (Filter Panel tidak dibuka).
- API pendukung di luar sumber modul disediakan tim FE: identitas pengguna dan payload izin Total Control (akses Admin Console > Activity Log), menu, dan flag Guided Tooltip `guided_tooltip_seen_ac-activity-log` yang dijawab seen agar walkthrough otomatis tidak menutupi layar.
- Kemampuan teknis (disediakan tim FE): mengamati unduhan berkas (ada atau tidak ada berkas terunduh).
- Tidak ada data backend atau state global yang diubah; pemulihan: semua mock dilepas di hook `after` walau spec gagal di tengah.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACAL-09: Error load tabel, kedua tab (bukan empty state)

1. Ganti mock List Session dan List User Action ke respons 5xx, lalu muat ulang Admin Console > Activity Log > Session
2. Verifikasi tab Session: alert `Unable to load this data.`
3. Verifikasi tab Session: tombol `[Try Again]` pada alert
4. Verifikasi tab Session: empty state `No activity yet` tidak tampil
5. Klik tab "User Action"
6. Verifikasi tab User Action: alert `Unable to load this data.`
7. Verifikasi tab User Action: tombol `[Try Again]` pada alert
8. Verifikasi tab User Action: empty state tidak tampil

### TC-AC-ACAL-10: Klik [Try Again] memuat ulang data, kedua tab

9. Ganti mock List Session dan List User Action ke respons 5xx pada permintaan pertama lalu normal pada permintaan berikutnya, lalu muat ulang Admin Console > Activity Log > Session
10. Tunggu alert error tampil pada tab Session
11. Klik `[Try Again]`
12. Verifikasi tab Session: alert hilang
13. Verifikasi tab Session: tabel normal tampil
14. Verifikasi tab Session: pagination tampil
15. Klik tab "User Action"
16. Tunggu alert error tampil pada tab User Action
17. Klik `[Try Again]`
18. Verifikasi tab User Action: alert hilang
19. Verifikasi tab User Action: tabel normal tampil
20. Verifikasi tab User Action: pagination tampil

### TC-AC-ACAL-131: Download gagal Tab Session, toast T-01

21. Ganti mock List Session dan List User Action ke respons normal, lalu muat ulang Admin Console > Activity Log > Session
22. Pasang mock Export Session dengan respons 5xx
23. Klik Download pada tab Session, pilih `Download as CSV`
24. Verifikasi toast error `Error, failed to download Activity-Log-Session.`
25. Verifikasi tidak ada berkas terunduh
26. Verifikasi tab Session: tabel tetap tampil

### TC-AC-ACAL-132: Download gagal Tab User Action, toast T-02

27. Klik tab "User Action"
28. Pasang mock Export User Action dengan respons 5xx
29. Klik Download pada tab User Action, pilih `Download as XLSX`
30. Verifikasi toast error `Error, failed to download Activity-Log-User-Action.`

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-09, 10, 131, 132). Tidak ada TC hanya-BE di spec ini.
- Kelas harness b (fault injection / resilience) untuk seluruh spec; `Mode: mock` menurut bagian 6 (resilience) karena hanya perilaku FE atas respons mock yang diasersi.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1, 9, 21, 22, dan 28 (mengganti atau memasang mock sesuai precondition tiap TC dan memuat ulang halaman), langkah 10 dan 16 (menunggu alert), dan langkah 27 (berpindah ke tab User Action untuk TC-132).
- Pada TC-10 asersi alert hilang (state sementara) ditaruh segera setelah pemicu `[Try Again]` dan sebelum asersi tabel; alert yang tampil pada langkah 10 dan 16 menjadi anchor positifnya.
- Pada TC-131 asersi "tidak ada berkas terunduh" didahului `Verifikasi` toast error yang membuktikan respons gagal sudah diproses (anchor; bagian 8b butir 2); Expected TC menyebut ketiganya dalam satu butir dan spec memecahnya per klausa (S-01).
- Temuan untuk QA:
  - Daftar endpoint spec ini memakai path, method, dan skema respons dari `openapi.yaml` dan `low-level-design.md` modul. Kedua dokumen tidak mendefinisikan endpoint stream real-time (SSE) untuk tab Session maupun User Action, padahal TC menyebut stream (NC-04); path dan skema event stream perlu ditetapkan pemilik API, dan spec ini hanya menyatakan koneksi terbuka tanpa event.
  - Dokumen API hanya mendefinisikan jawaban 500 berupa `{ "message": "Internal server error" }`; bentuk jawaban 5xx lain (mis. 502/503/timeout) tidak didefinisikan, sehingga mock 5xx memakai 500.
  - TC-09 mensyaratkan 5xx pada endpoint List kedua tab tanpa menyebut apakah SSE ikut gagal; spec menjawab stream terbuka tanpa event.
  - TC-10 tidak menyebut apakah "permintaan pertama" dihitung per tab atau global; spec memakai respons 5xx pada permintaan pertama tiap tab.
  - TC-131 dan TC-132 menyebut "Download > CSV" dan "Download > XLSX"; spec memakai label overlay `Download as CSV` dan `Download as XLSX` dari PRD §4.2.
  - TC-132 hanya mengasersi toast; "tidak ada berkas" dan "tabel tetap" tidak ada di Expected dan tidak diasersi.
  - Email akun Pre-setup memakai placeholder `{namaCompany}`; pada spec mock akun hanya dimodelkan lewat payload izin.
