---
id: TC-GS-ACTLOG-E2E-044-opsi-filter-indikator-pemuatan-dan-sumber-kosong
title: "Opsi Filter: Indikator Pemuatan dan Sumber Kosong"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-113
  - TC-GS-ACTLOG-114
coverage:
  web: automated
---

# Opsi Filter: Indikator Pemuatan dan Sumber Kosong

## Prerequisites

- Mode: mock.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`. Seluruh API di-mock (mock server FE) sehingga tidak ada login ke backend nyata dan tidak ada password yang dipakai. API pendukung halaman di luar sumber modul (identitas pengguna, menu, dan flag Guided Tooltip halaman Activity Log, dijawab sebagai seen) disediakan tim FE; kontraknya di luar sumber modul ini.
- Kebutuhan mock (semua endpoint yang dipanggil halaman pada kondisi tes, dari `global-settings/activity-log/API/openapi.yaml` dan `low-level-design.md`):
  - `POST /v2/analytics-reporting/session-logs/list` dan `POST /v2/analytics-reporting/change-logs/list` (openapi baris 12 dan 238): jawaban 200 `{ message, data: { totalRecords, data[] } }` (openapi baris 44-57 dan skema list Session 749-758; skema list User Action mengikuti `change-logs/list`). Pada TC-GS-ACTLOG-113 menjawab daftar berisi baris (`Fixture.activityLog.mockListSession` dan `Fixture.activityLog.mockListUserAction`, fixture baru); pada TC-GS-ACTLOG-114 menjawab 0 baris (`totalRecords` 0, `data` kosong).
  - `POST /v2/analytics-reporting/session-logs/options` dan `POST /v2/analytics-reporting/change-logs/options` (openapi baris 102 dan 359): jawaban 200 `{ message: "Options retrieved", data: { ...facet yang diminta } }` (openapi baris 966-1033 dan 1071-1133). Pada TC-GS-ACTLOG-113 jawaban ditahan (respons lambat) sampai dilepas, lalu menjawab 200 sesuai skema itu; pada TC-GS-ACTLOG-114 menjawab 200 tanpa `data` (sumber kosong, `low-level-design.md` Logic langkah 4 tiap endpoint options).
  - `GET /v2/analytics-reporting/session-logs/stream` dan `GET /v2/analytics-reporting/change-logs/stream` (openapi baris 495-577, `low-level-design.md` baris 386-490): jawaban 200 `text/event-stream` yang dibuka dan tidak mengirim event `session_logs.created` atau `change_logs.created`, pada kedua TC.
  - Endpoint Download tidak dipanggil spec ini dan tidak di-mock.
  - Tiap pemicu dipasang di mock server FE dan dilepas segera setelah asersinya selesai.
- State global yang diubah: tidak ada; seluruh pemicu hidup di mock dan dilepas oleh langkah pemulihan, dengan hook `after` sebagai cadangan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ACTLOG-113: Indikator pemuatan pada daftar opsi filter yang diambil dari data tabel

1. Pasang mock yang menahan respons `POST /v2/analytics-reporting/session-logs/options` dan `POST /v2/analytics-reporting/change-logs/options`, dengan respons list berisi baris
2. Buka Global Settings > Activity Log > Tab "Session", klik icon Filter, buka daftar opsi field User
3. Verifikasi skeleton atau spinner mini tampil di dalam daftar opsi field User Tab Session, bukan daftar kosong tanpa indikator
4. Tutup daftar opsi dan Filter Panel tanpa [Apply], lalu klik tab "User Action", klik icon Filter, buka daftar opsi field Action
5. Verifikasi skeleton atau spinner mini tampil di dalam daftar opsi field Action Tab User Action, bukan daftar kosong tanpa indikator

### Pemulihan state antar TC

6. Lepaskan tahanan respons options, tutup daftar opsi dan Filter Panel tanpa [Apply]

### TC-GS-ACTLOG-114: Daftar opsi filter saat tabel sumber kosong

7. Pasang mock yang menjawab respons list dan options kosong (0 baris) untuk kedua tab
8. Muat ulang halaman Global Settings > Activity Log > Tab "Session", klik icon Filter, buka daftar opsi field User
9. Verifikasi tidak ada toast error di Tab Session
10. Verifikasi daftar opsi Tab Session menampilkan teks `"No options available"`
11. Verifikasi tidak ada pesan error di dalam daftar opsi Tab Session
12. Verifikasi state kosong `"No activity yet"` tampil di tabel Tab Session
13. Verifikasi tidak ada error state tabel (`"Unable to load this data."` dan `[Try Again]`) di Tab Session
14. Tutup daftar opsi dan Filter Panel tanpa [Apply], lalu klik tab "User Action", klik icon Filter, buka daftar opsi field Action
15. Verifikasi tidak ada toast error di Tab User Action
16. Verifikasi daftar opsi Tab User Action menampilkan teks `"No options available"`
17. Verifikasi tidak ada pesan error di dalam daftar opsi Tab User Action
18. Verifikasi state kosong `"No activity yet"` tampil di tabel Tab User Action
19. Verifikasi tidak ada error state tabel (`"Unable to load this data."` dan `[Try Again]`) di Tab User Action

### Pemulihan state akhir

20. Tutup daftar opsi dan Filter Panel tanpa [Apply], lalu lepaskan mock list dan options

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md`. Kelas harness b (fault injection): kedua TC memicu respons options yang ditahan atau kosong lewat mock.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1 dan 7 (memasang mock sesuai Precondition TC), langkah 4 dan 14 (menutup panel dan pindah tab), serta langkah pemulihan 6 dan 20.
- Asersi absence "tidak ada pesan error" dipecah per surface (toast, daftar opsi, error state tabel). Toast ditaruh segera setelah pemicu (8b.11); asersi daftar opsi dan error state tabel didahului anchor positif pada surface yang sama (`"No options available"` pada daftar opsi, `"No activity yet"` pada tabel, PRD §7 S-02). Langkah 12 dan 18 adalah asersi tambahan di luar Expected TC untuk anchor itu (S-03).
- Temuan untuk QA:
  - TC-113 menyebut "network throttle" sebagai pemicu; spec memakai tahanan respons pada endpoint options di mock.
  - TC-114 menulis "Respons List dan opsi filter kosong (di-intercept)" tanpa menyebut apakah Filter Panel tetap dapat dibuka saat tabel kosong; spec mengikuti langkah TC (Filter Panel dibuka).
  - Bentuk badan respons list dan options tidak diuraikan di TC; bentuknya mengikuti skema `openapi.yaml` dan disiapkan tim FE.
  - Post Condition kedua TC bernilai `-`; tidak diasersi.
