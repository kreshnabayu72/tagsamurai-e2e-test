---
id: TC-GS-NLU-E2E-004-tampilan-kolom-last-update-switch-active-tooltip-table-tools
title: "Tampilan kolom Last Update, switch Active, tooltip Table Tools, dan overlay row action"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-16
  - TC-GS-NLU-17
  - TC-GS-NLU-18
  - TC-GS-NLU-19
coverage:
  web: automated
---

# Tampilan kolom Last Update, switch Active, tooltip Table Tools, dan overlay row action

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza, Default User entitas), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` untuk akun aktor sudah diset true oleh hook suite `before` (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: Non-Login User Budi Kurniawan (Active) dan Joko Susilo (Inactive manual) (No. 11) hanya dibaca. General Settings client: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone `Asia/Jakarta` (Pre-setup No. 16) dibaca, tidak diubah.
- Spec hanya membaca; Search yang dipakai dipulihkan lewat langkah penghubung. Tidak ada state global yang diubah.
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.
- Suite berjalan serial (`parallel: false`).
- Env var yang dipakai terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-GS-NLU-16: Kolom Last Update mengikuti format tanggal dan jam General Settings

1. Klik icon Search, ketik Search `Budi Kurniawan`, tekan Enter
2. Verifikasi tanggal dan jam sel Last Update baris Budi Kurniawan tampil sesuai Date Format `dd/MM/yy`, Time Format 24 jam, dan Timezone `Asia/Jakarta` General Settings client

### TC-GS-NLU-17: Tampilan switch Active ON dan OFF pada tabel

3. Verifikasi switch Active baris Budi Kurniawan (ON) berwarna primary Global Settings
4. Ganti isi kotak search dengan `Joko Susilo`, tekan Enter
5. Verifikasi switch Active baris Joko Susilo (OFF) netral (inactive)

### TC-GS-NLU-18: Tooltip icon Table Tools dan header kolom Actions

6. Klik `(←)` pada kotak Search agar icon Table Tools tampil
7. Hover icon Search
8. Verifikasi Tooltip `Search`
9. Hover icon Filter
10. Verifikasi Tooltip `Filter`
11. Hover icon Download
12. Verifikasi Tooltip `Download`
13. Hover icon Changelog
14. Verifikasi Tooltip `Changelog`
15. Hover icon `⋯` pada header kolom Actions
16. Verifikasi Tooltip `Column Visibility`

### TC-GS-NLU-19: Overlay row action Total Control menampilkan Detail, Edit, Convert to Login User, Delete

17. Klik icon Search, ketik Search `Budi Kurniawan`, tekan Enter
18. Klik ikon `⋯` pada baris Budi Kurniawan
19. Verifikasi Overlay row action berisi berurutan: `Detail`, `Edit`, `Convert to Login User`, `Delete`
20. Verifikasi opsi `Delete` bergaya destruktif (danger)

## Notes

- Langkah penghubung (S-03, R-16): langkah 1, 4, 6, 17 (Search untuk menemukan baris target dan mengosongkan Search agar icon Table Tools tampil).
- Temuan untuk QA:
  - TC-GS-NLU-16 Expected tidak menyebut string tanggal dan jam persisnya; spec mengasersi kesesuaian dengan format General Settings client (nilai `dd/MM/yy`, 24 jam, `Asia/Jakarta` dari Pre-setup No. 16), bukan string literal.
  - TC-GS-NLU-17 dan TC-GS-NLU-19 langkah TC "Amati" baris Budi Kurniawan dan Joko Susilo; keduanya diamati bergantian lewat Search karena bukan pada halaman yang sama dijamin.
- Lampiran A konvensi tidak memuat butir untuk modul Non-Login User; tidak ada pengecualian khusus modul yang dipakai.
