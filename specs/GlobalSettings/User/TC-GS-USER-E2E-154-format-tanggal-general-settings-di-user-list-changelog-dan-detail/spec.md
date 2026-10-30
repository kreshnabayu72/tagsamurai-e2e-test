---
id: TC-GS-USER-E2E-154-format-tanggal-general-settings-di-user-list-changelog-dan-detail
title: "Format Tanggal General Settings di User List, Modal Changelog, dan User Detail"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-965
  - TC-GS-USER-966
  - TC-GS-USER-967
coverage:
  web: automated
---

# Format Tanggal General Settings di User List, Modal Changelog, dan User Detail

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User). Spec memakai satu akun tanpa ganti akun. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- State global yang diubah: General Settings entitas Date Format, Time Format, dan Timezone. Hook `before` membaca nilai awal ketiganya lalu mengaturnya menjadi Date Format `MM/DD/YYYY`, Time Format 12-hour, Timezone `Asia/Makassar` (UTC+8) sesuai precondition c TC; hook `after` memulihkan ketiganya ke nilai awal dan tetap jalan walau spec gagal di tengah. Kemampuan mengubah dan memulihkan General Settings lewat API dengan akun Total Control disediakan tim FE/BE (TC dan PRD tidak memberi cara). Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10 sampai 22) tidak dipakai dan tidak diubah; spec memakai user milik sendiri (S-06).
- Data Dinamis (suffix per run dan nomor spec), di-seed lewat API di hook `before` oleh akun Total Control (kemampuan seeding Login User lewat API; nilai field wajib lain user mengikuti fixture `fixtures/user.json` yang belum ada, disediakan tim FE):
  - Login User `Wawan Setiawan {runId}-154`, email `wawansetiawan+{runId}-154@qwertysystem.net`, Activated, Active, Access `Fixed Asset`, Temporary User dengan Temporary Until = tanggal kalender hari ini + 30 hari pada zona waktu `Asia/Makassar`, dicatat sebagai `{tempUntil}`.
  - Hook `before` membaca lewat fixture BE cap waktu mentah (UTC) kolom Last Update user itu sebagai `{T_lu}` dan cap waktu mentah entri Changelog `Create` user itu sebagai `{T_cl}`; nilai tampilan yang diharapkan adalah cap waktu mentah dikonversi ke `Asia/Makassar` dan diformat `MM/DD/YYYY` dengan jam 12-hour (AM/PM). `{tglLu}` dan `{tglCl}` adalah tanggal kalender `{T_lu}` dan `{T_cl}` pada `Asia/Makassar`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan General Settings ke nilai awal, lalu hapus lewat API Login User `wawansetiawan+{runId}-154@qwertysystem.net`.

## Test Steps

### TC-GS-USER-965: Format tanggal General Settings berlaku di User List (Last Update)

1. Klik icon Search, ketik `Wawan Setiawan {runId}-154`, tekan Enter
2. Verifikasi Last Update baris `Wawan Setiawan {runId}-154` tampil dengan format tanggal `MM/DD/YYYY`
3. Verifikasi jam pada Last Update baris `Wawan Setiawan {runId}-154` berformat 12-hour dengan penanda AM/PM
4. Verifikasi Last Update baris `Wawan Setiawan {runId}-154` sama dengan `{T_lu}` yang dikonversi ke `Asia/Makassar`
5. Buka Filter Panel
6. Pilih tanggal `{tglLu}` pada input filter Last Update lewat date picker
7. Verifikasi input filter Last Update menampilkan tanggal dengan format `MM/DD/YYYY`
8. Tutup Filter Panel tanpa Apply

### TC-GS-USER-966: Format tanggal General Settings berlaku di Modal Changelog User

9. Klik icon Changelog pada Table Tools
10. Klik icon Search di Modal Changelog, ketik `Wawan Setiawan {runId}-154`, tekan Enter
11. Verifikasi Date baris `Create` `Wawan Setiawan {runId}-154` di Modal Changelog tampil dengan format tanggal `MM/DD/YYYY`
12. Verifikasi jam pada Date baris `Create` berformat 12-hour dengan penanda AM/PM
13. Verifikasi Date baris `Create` sama dengan `{T_cl}` yang dikonversi ke `Asia/Makassar`
14. Buka filter Date di Modal Changelog
15. Pilih tanggal `{tglCl}` pada input filter Date lewat date picker
16. Verifikasi input filter Date menampilkan tanggal dengan format `MM/DD/YYYY`
17. Tutup Modal Changelog lewat `✕`

### TC-GS-USER-967: Format tanggal General Settings berlaku di User Detail

18. Klik Name `Wawan Setiawan {runId}-154`
19. Verifikasi Temporary until pada Detail tampil dengan format tanggal `MM/DD/YYYY`
20. Verifikasi Temporary until pada Detail sama dengan `{tempUntil}`
21. Klik Tab `Changelog` pada Detail
22. Verifikasi Date baris `Create` pada Tab Changelog tampil dengan format tanggal `MM/DD/YYYY`
23. Verifikasi jam pada Date baris `Create` berformat 12-hour dengan penanda AM/PM
24. Verifikasi Date baris `Create` sama dengan `{T_cl}` yang dikonversi ke `Asia/Makassar`
25. Buka filter Date di Tab Changelog
26. Pilih tanggal `{tglCl}` pada input filter Date lewat date picker
27. Verifikasi input filter Date menampilkan tanggal dengan format `MM/DD/YYYY`
28. Kembali ke User List dengan klik Back

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Kelas h (prinsip 13h; state tenant: General Settings Date Format, Time Format, dan Timezone entitas diubah dan dipulihkan); tiga TC memuat hanya kelas itu.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 5, 9, 10, 14, 18, 21, 25 (membuka layar, Search, dan filter); langkah 6, 15, 26 (memilih tanggal pada date picker, aksi TC "memilih tanggal"); langkah 8 dan 17 (menutup Filter Panel dan Modal Changelog); langkah 28 (Back ke User List).
- Expected Result a tiap TC (tanggal, jam, konversi) dipecah menjadi tiga `Verifikasi` per klausa (S-01); expected b memakai satu `Verifikasi` per input filter.
- Pada TC-GS-USER-967 klausa jam dan konversi diasersi pada Date baris log Tab Changelog; Temporary until (langkah 19 dan 20) diasersi format tanggal dan nilai saja.
- Pemakaian Modal Changelog User (langkah 9 sampai 17) memakai Search nama seed bersuffix untuk mengidentifikasi entri `Create` user, bukan posisi teratas (S-12).
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-USER-965, 966, 967: TC tidak menyebut nilai awal General Settings, cara mengubahnya, dan cara memulihkannya; disediakan tim FE/BE (S-13).
  - TC-GS-USER-965, 966, 967: TC tidak menyebut pola jam 12-hour (contoh `hh:mm A`) dan tidak menyebut tanggal mana yang dipilih pada date picker; spec memilih tanggal kalender cap waktu seed pada `Asia/Makassar` dan mengasersi penanda AM/PM.
  - TC-GS-USER-967: "Temporary until" tidak menyebut apakah memuat jam; spec hanya mengasersi format tanggal dan nilainya. TC menyebut "tab log" tanpa menyatakan tab mana; spec memakai Tab Changelog.
  - TC-GS-USER-965: TC menyebut "input date filter" tanpa menyebut filter yang dimaksud; spec memakai filter Last Update pada Filter Panel User List.
