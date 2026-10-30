---
id: TC-GS-GSET-E2E-044-multi-konteks-propagasi-sse-ke-tab-lain
title: "SSE multi-tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-118
  - TC-GS-GSET-119
  - TC-GS-GSET-120
coverage:
  web: automated
---

# SSE multi-tab

## Prerequisites

- Mode: FE+BE.
- Akun Tab 1 dan Tab 2 (satu pengguna, satu konteks browser, sesi login yang sama): Total Control, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; Tab 1 berada di Global Settings > General Settings. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.
- Akun Admin B (pelaku perubahan state pada TC-GS-GSET-120, hanya lewat sesi API tanpa login UI): Total Control, Andi Wijaya, `totalControlGlobalSettingsB_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No 2), kredensial `Spectra.env.GS_TCB_PASSWORD` (nama env baru). Login API Admin B dilakukan di hook `before`. Hasil Save Admin B tidak diasersi di sesi UI Admin B (hanya di Tab 1), sehingga sesi UI kedua tidak dipakai (P-2 konvensi bagian 3 prinsip 13).
- Environment variable: `GS_TC_PASSWORD` dan `GS_TCB_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `GS_TCB_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example` (didaftarkan pada tahap script).
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan record ke baseline Pre-setup No 10): lihat `suite.md`, bagian Hook suite; spec ini tidak mengatur flag sendiri.
- Data: record General Settings Client A pada baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`). Nilai yang disimpan: TC-GS-GSET-118 Date Format `M/d/yy`; TC-GS-GSET-119 Session Idle Timeout `1 hour`; TC-GS-GSET-120 Time Format `hh:mm a` (oleh Admin B). Spec tidak membuat data dinamis.
- Permukaan Tab 2: Admin Console > Client List, kolom Last Updated (konsumen format tanggal dari General Settings; sesuai TC-GS-GSET-118).
- Kemampuan teknis: (a) dua tab dalam satu konteks browser, dengan langkah ditandai `[Tab 1]` dan `[Tab 2]`; (b) menjalankan skrip pada halaman Tab 2 untuk memasang dan membaca penanda di dokumen (`window.__gsetMarker`), yang dipakai membuktikan halaman tidak dimuat ulang; (c) sesi API Total Control untuk memulihkan record Client A ke baseline Pre-setup No 10 lewat PUT `/v2/enterprise-management/general-settings` (`API/openapi.yaml`), dan sesi API Admin B untuk PUT serta GET endpoint yang sama (klien HTTP dan penangkapan token disediakan tim FE); (d) jeda nyata 5 detik pada langkah 15 dan 26 sebagai jendela bagi event SSE (durasi dipilih spec sebagai jendela amat; TC tidak menyebut durasi).
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- State global yang diubah: Date Format (TC-GS-GSET-118), Session Idle Timeout (TC-GS-GSET-119), dan Time Format (TC-GS-GSET-120) record General Settings Client A, dipulihkan lewat langkah 9, 23, dan 29 serta hook `beforeEach` dan `after` suite. Tab 2 ditutup pada langkah 23 dan di hook `after` bila masih terbuka (S-09). Suite berjalan serial (`parallel: false`).
- Layar awal Global Settings > General Settings dibuka di hook `beforeEach` (konvensi bagian 4).

## Test Steps

### TC-GS-GSET-118: Perubahan format dari General Settings terlihat tanpa reload di surface konsumen yang sedang terbuka

1. [Tab 2] Buka tab baru di konteks browser yang sama, buka Admin Console > Client List, catat teks kolom Last Updated baris pertama sebagai `{tglAwal}`, lalu pasang penanda `window.__gsetMarker` pada dokumen
2. [Tab 1] Pilih Date Format `M/d/yy`
3. [Tab 1] Klik `[Save]`
4. [Tab 1] Tunggu aksi selesai (tombol `[Save]` disabled kembali)
5. Pindah ke Tab 2 tanpa memuat ulang halaman
6. [Tab 2] Verifikasi kolom Last Updated pada Client List menampilkan tanggal baris pertama dalam format `M/d/yy` (sebelumnya `{tglAwal}` dalam format `dd/MM/yy`)
7. [Tab 2] Verifikasi tidak ada dialog interupsi
8. [Tab 2] Verifikasi halaman tidak dimuat ulang (penanda `window.__gsetMarker` masih ada)
9. Pulihkan record Client A ke baseline Pre-setup No 10 lewat sesi API

### TC-GS-GSET-119: Perubahan Session Idle Timeout tetap dipush ke consumer tanpa memutus sesi dan tanpa dialog

10. [Tab 2] Tunggu hingga kolom tanggal baris pertama kembali berformat `dd/MM/yy`, lalu catat teks tanggal baris pertama sebagai `{tglSebelum}`
11. [Tab 1] Muat ulang halaman (F5), lalu pilih Session Idle Timeout `1 hour`
12. [Tab 1] Klik `[Save]`
13. [Tab 1] Tunggu aksi selesai (tombol `[Save]` disabled kembali)
14. Pindah ke Tab 2 tanpa memuat ulang halaman
15. [Tab 2] Tunggu 5 detik tanpa memuat ulang halaman
16. [Tab 2] Verifikasi tidak ada dialog
17. [Tab 2] Verifikasi tampilan tidak berubah (teks tanggal baris pertama sama dengan `{tglSebelum}`)
18. [Tab 2] Klik satu item menu sidebar Admin Console yang berbeda dari halaman aktif
19. [Tab 2] Verifikasi sesi Tab 2 tetap aktif (halaman hasil klik menu tampil, bukan halaman login dan bukan Dialog Session Expired)
20. [Tab 1] Muat ulang halaman (F5)
21. [Tab 1] Verifikasi sesi Tab 1 tetap aktif (halaman Global Settings > General Settings tampil, bukan halaman login dan bukan Dialog Session Expired)
22. [Tab 1] Verifikasi Session Idle Timeout tetap `1 hour` (tidak di-reset)
23. Pulihkan record Client A ke baseline Pre-setup No 10 lewat sesi API, tutup Tab 2, lalu muat ulang halaman Tab 1 (F5)

### TC-GS-GSET-120: Halaman General Settings yang sedang terbuka tidak auto-refresh akibat event SSE

24. [Admin B] Simpan Time Format `hh:mm a` lewat sesi API (field lain sama dengan nilai tersimpan) hingga tersimpan
25. [Admin B] Verifikasi GET `/v2/enterprise-management/general-settings` mengembalikan `timeFormat` `hh:mm a`
26. [Tab 1] Tunggu 5 detik tanpa memuat ulang halaman
27. [Tab 1] Verifikasi Select Time Format tetap `HH:mm`
28. [Tab 1] Verifikasi tidak ada dialog
29. Pulihkan record Client A ke baseline Pre-setup No 10 lewat sesi API

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (TC-GS-GSET-118, 119, 120). Mode: FE+BE. Kelas: multi-konteks (multi-tab, prinsip 13 butir c); Tab 2 menjadi objek asersi (bukan pemicu P-2).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 4, 5, 9 sampai 15, 18, 20, 23, 24, dan 26 (membuka dan menutup tab, memasang penanda, menunggu Save selesai, pindah tab, pemulihan baseline, dan jeda).
- Langkah 25 adalah `Verifikasi` tambahan di luar Expected TC yang berfungsi sebagai anchor positif untuk asersi tidak berubah pada langkah 27 (bagian 8b butir 2): perubahan Admin B benar-benar tersimpan di server.
- Tab 1 pada TC-GS-GSET-120 dibaca setelah pemulihan dan muat ulang pada langkah 23, sehingga Time Format form awal `HH:mm` (precondition TC).
- Pada TC-GS-GSET-119 langkah 10 menunggu push pemulihan baseline sampai Tab 2 kembali berformat `dd/MM/yy`, supaya `{tglSebelum}` dicatat pada format baseline. Langkah ini tidak diasersi karena bukan Expected TC; bila push tidak tiba, kegagalannya terlihat pada langkah 6.
- TC-GS-GSET-118 Post Condition (konsumen terdampak lain: FAMS, SAMS, file Download/Export semua modul "dedicated di file modul masing-masing") tidak punya langkah observasi dan tidak diasersi.
- Temuan untuk QA:
  - TC-GS-GSET-119 Expected "sesi tab 1 dan tab 2 tetap aktif (tidak diputus dan tidak di-reset)" tidak menyebut tampilan yang teramati. Spec mengasersi bahwa halaman tetap termuat (bukan halaman login dan bukan Dialog Session Expired, `auth-foundation.md` §6 dan §7) serta nilai Session Idle Timeout tidak berubah; "tidak di-reset" untuk timer idle tidak punya cara observasi di TC.
  - TC-GS-GSET-119 langkah 3 ("aksi apa pun di tab 2") tidak menyebut aksi; spec memilih klik item menu sidebar Admin Console.
  - TC-GS-GSET-119 dan TC-GS-GSET-120 Expected absence ("tidak ada dialog dan tidak ada perubahan tampilan"; "tidak berubah") tidak menyebut jendela amat atau durasi tunggu; spec menambah jeda 5 detik tanpa memuat ulang halaman (langkah 15 dan 26) sebelum asersi absence.
  - TC-GS-GSET-120: precondition menyebut Admin B berada di tab terpisah pada General Settings; spec memakai sesi API Admin B karena hasil di sesi itu tidak diasersi.
