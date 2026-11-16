---
id: TC-FA-TDC-E2E-217-request-langsung-starter-suspended-bypass-ui-dan-rate-dari-klien-diabaikan
title: "Request Langsung: Plan Starter dan Entitas Suspended Ditolak serta Rate dari Klien Diabaikan"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-173
  - TC-FA-TDC-831
  - TC-FA-TDC-888
sourceRules: ["T-01", "FATDC-LOGIC-03f.1", "FATDC-LOGIC-03f.2", "FATDC-LOGIC-03f.5", "E-FATDC-62"]
smoke: []
dependsOn: []
trace:
  "T-01": 11
  "FATDC-LOGIC-03f.1": 13
  "FATDC-LOGIC-03f.2": 13
  "FATDC-LOGIC-03f.5": 13
  "E-FATDC-62": [24, 26]
anchor: [18, 20]
coverage:
  web: automated
---

# Request Langsung: Plan Starter dan Entitas Suspended Ditolak serta Rate dari Klien Diabaikan

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset); password lewat `Spectra.env.FA_TC_PASSWORD`. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung dan request baca, seed dan pemulihan lewat API, serta perubahan plan company dan status company (disediakan tim FE/BE). Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- Kemampuan intercept: `Spectra.intercept()` di atas backend nyata untuk menambah field rate pada payload request Create (TC-FA-TDC-173); intercept dilepas segera setelah pemicu selesai (S-09).
- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsS1` | `KHS-S1` | belum ada di daftar; dibuat langkah 1 sampai 11 dan dihapus langkah 15 |
| `nb4` | `NB-4` | Class Name `Bukan bangunan – Kelompok 4`, Active, Used By 0 |

- Data Dinamis TC-FA-TDC-173: Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`); Class Name `Kelompok S1 uji`. Master Data Count Limit belum tercapai. Tabel berisi tujuh class seed bawaan, sehingga dengan `KHS-S1` tabel berisi 8 baris dalam satu halaman Pagination (10 baris per halaman).
- State global yang diubah spec: plan company (Growth ke Starter, langkah 16, dipulihkan langkah 21) dan status entitas client (Suspended, langkah 22, dipulihkan langkah 27); hook `after` memulihkan keduanya bila spec berhenti di tengah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-173: Rate yang tersimpan adalah hasil hitung server, bukan nilai dari klien

1. Klik `+ Class` di toolbar
2. Isi Regulation Reference `UU HPP 7/2021; PMK 72/2023`
3. Isi Class Code `KHS-S1`
4. Isi Class Name `Kelompok S1 uji`
5. Pilih Asset Type `Non-building`
6. Isi Useful Life `8`
7. Pilih Allowed Methods `Straight Line` dan `Declining Balance`
8. Aktifkan intercept request Create: tambahkan Straight Line Rate `99` dan Declining Balance Rate `99` pada payload sebelum terkirim
9. Klik `[Submit]`
10. Lepas intercept request Create
11. Verifikasi muncul toast sukses: "Success, tax depreciation class has been created."
12. Ketik Search `KHS-S1`, tekan Enter
13. Verifikasi baris `KHS-S1` menampilkan Straight Line Rate "12.5%" dan Declining Balance Rate "25%"
14. Klik `(←)` pada kotak Search
15. Hapus class `KHS-S1` lewat API hingga terhapus

### TC-FA-TDC-831: Request tulis langsung pada plan Starter ditolak Forbidden

16. Turunkan plan company dari Growth ke Starter (data class tetap tersimpan)
17. Kirim request langsung dengan sesi API aktor Total Control untuk mengubah Class Name `NB-4` menjadi `Kelompok 4 Starter` tanpa melalui UI
18. Verifikasi server menolak request dengan 403 Forbidden
19. Baca ulang class `NB-4` lewat request baca
20. Verifikasi Class Name `NB-4` tetap `Bukan bangunan – Kelompok 4`
21. Pulihkan plan company ke Growth

### TC-FA-TDC-888: Request langsung Deactivate saat entitas Suspended ditolak server

22. Ubah status entitas client menjadi Suspended
23. Kirim request langsung dengan sesi API aktor Total Control untuk menonaktifkan class `NB-4` tanpa melalui UI
24. Verifikasi server menolak request dengan 403 Forbidden walau aktor adalah Total Control
25. Baca ulang status `NB-4` lewat request baca
26. Verifikasi status `NB-4` tetap Active
27. Pulihkan status entitas client ke Active

## Notes

- K-1: TC-FA-TDC-831 dan TC-FA-TDC-888 (kelas a dengan Expected respons API) tetap masuk spec FE+BE; keduanya hanya mengasersi status respons dan state data lewat request baca (8b.1). TC-FA-TDC-173 berjalan lewat UI dengan payload dimanipulasi oleh intercept, sehingga toast dan isi baris tabel diasersi.
- P-5 butir (b): TC-FA-TDC-831 (plan Starter) dan TC-FA-TDC-888 (entitas Suspended) adalah objek uji ringan kelas h; state tenant hanya mengondisikan request langsung yang menjadi objek uji (kelas a), tanpa harness eksternal dan tanpa state berat. Dua TC kelas h berada di spec ini bersama satu TC kelas a.
- Klausa Expected c TC-FA-TDC-831 dan TC-FA-TDC-888 (tidak ada entri log baru) tidak diasersi di spec ini; asersinya ada di spec absence 262 dengan aksi nyata dan baseline sendiri per TC (S-05).
- Langkah penghubung (S-03): langkah 12 dan 14 (Search `KHS-S1` untuk menemukan baris target, 8b.13, R-16, lalu mengosongkan Search); langkah 15 (menghapus class milik spec); langkah 16, 21, 22, dan 27 (mengubah dan memulihkan plan company dan status entitas client sebagai pemicu).
- Urutan TC: TC-FA-TDC-173, 831, 888; blok yang mengubah plan dan status tenant di akhir spec dan dipulihkan sebelum blok berikutnya.
- Temuan untuk QA:
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
  - TC-FA-TDC-173 menyebut "form valid" tanpa Regulation Reference dan Class Name; spec memakai Regulation Reference `UU HPP 7/2021; PMK 72/2023` dan Class Name `Kelompok S1 uji`.
  - TC-FA-TDC-173 tidak menyebut mekanisme "Ubah payload request sebelum terkirim"; spec memakai intercept request Create.
  - Akun pelaku perubahan plan dan status client tidak disebut TC; kemampuannya disediakan tim FE/BE (S-13).
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
