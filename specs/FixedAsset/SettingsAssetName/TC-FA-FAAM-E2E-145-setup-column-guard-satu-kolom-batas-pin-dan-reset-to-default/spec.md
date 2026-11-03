---
id: TC-FA-FAAM-E2E-145-setup-column-guard-satu-kolom-batas-pin-dan-reset-to-default
title: "Setup Column: Guard Satu Kolom Tersisa, Batas Pin Tiga Kolom, dan Reset to Default"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-425
  - TC-FA-FAAM-427
  - TC-FA-FAAM-428
coverage:
  web: automated
---

# Setup Column: Guard Satu Kolom Tersisa, Batas Pin Tiga Kolom, dan Reset to Default

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`).
- Kemampuan teknis: drag and drop, scroll horizontal tabel, hapus preferensi kolom di browser (disediakan tim FE).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: konfigurasi kolom tabel utama (preferensi di browser) diubah spec ini. Pemulihan: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-427: Guard satu kolom tersisa: checkbox disabled dengan tooltip
1. Buka Popup Setup Column: klik header kolom Actions (⋯), lalu `Setup Column...`
2. Uncheck 11 kolom sehingga tersisa satu kolom visible
3. Arahkan kursor ke checkbox kolom tersisa
4. Verifikasi checkbox kolom tersisa disabled dengan tooltip `At least one column must remain visible.`
5. Klik `[✕]`
### TC-FA-FAAM-428: Pin keempat dibatasi maksimal tiga kolom
6. Buka Popup Setup Column
7. Pin tiga kolom
8. Arahkan kursor ke icon Pin kolom ke-4
9. Verifikasi icon Pin kolom ke-4 disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
10. Klik `[✕]`
### TC-FA-FAAM-425: Reset to Default mengembalikan seluruh konfigurasi kolom setelah Save
11. Buka Popup Setup Column
12. Sembunyikan `Code`, geser `Brand` ke awal, pin `Asset Name`, lalu klik `[Save]`
13. Buka Popup Setup Column
14. Klik `[Reset to Default]`
15. Verifikasi Live Preview kembali default: 12 kolom Visible dengan urutan awal
16. Verifikasi Live Preview tanpa kolom ter-pin
17. Klik `[Save]`
18. Verifikasi tabel menampilkan konfigurasi default
19. Tekan F5
20. Verifikasi tabel tetap menampilkan konfigurasi default setelah F5

## Notes

- Urutan di spec: blok guard (TC-FA-FAAM-427 dan 428) lebih dulu karena ditutup dengan `[✕]` tanpa menyimpan, TC-FA-FAAM-425 terakhir karena menyimpan konfigurasi dengan `[Save]` (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`): membuka popup dan menutupnya dengan `[✕]`, yang membuang perubahan preview, sehingga tidak ada form dirty yang tertinggal.
- Verifikasi "tanpa kolom ter-pin" (TC-FA-FAAM-425) beranchor Verifikasi 12 kolom Visible pada Live Preview yang sama (bagian 8b butir 2).
- Pada TC-FA-FAAM-425 `[Reset to Default]` adalah objek uji; pemulihan akhir oleh hook `after` tetap menghapus preferensi kolom di browser.
