---
id: TC-AC-ACC-E2E-064-create-balapan-dua-sesi-company-name-sama
title: "Create Client: Dua Admin Menyimpan Company Name yang Sama Hampir Bersamaan (Dua Sesi)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-519
coverage:
  web: automated
---

# Create Client: Dua Admin Menyimpan Company Name yang Sama Hampir Bersamaan (Dua Sesi)

## Prerequisites

- Mode: FE+BE. Kelas multi-konteks (c): dua sesi browser independen.
- Akun aktor: Sesi A Total Control Principal (A-01) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`; Sesi B Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Sesi A login di hook `before`; Sesi B dibuka sebagai konteks browser kedua di hook `before`; hook `after` menutup Sesi B dan mengembalikan sesi ke akun default suite. Halaman Admin Console > Client dibuka hook `beforeEach` suite pada Sesi A; Sesi B membuka halaman yang sama pada langkah awal.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-064@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong.
- Dataset Dinamis: Company Name `PT Balapan Uji {runId}-064` pada kedua sesi; Default User Sesi A `Umar Hakim` (`umar.hakim+{runId}-064@qwertysystem.net`, Group `Cabang Menteng`), Sesi B `Vina Oktaviani` (`vina.oktaviani+{runId}-064@qwertysystem.net`, Group `Area Jakarta`).
- Kemampuan teknis: mengeksekusi klik `[Submit]` di dua sesi hampir bersamaan.
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

1. [Sesi A dan Sesi B] Klik `[+ New Client]`
2. [Sesi A] Isi Company Name `PT Balapan Uji {runId}-064`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name `Umar`, Last Name `Hakim`, Email `umar.hakim+{runId}-064@qwertysystem.net`, dan Division sesuai Data valid Create; pilih Group "Cabang Menteng"
3. [Sesi B] Isi Company Name `PT Balapan Uji {runId}-064`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name `Vina`, Last Name `Oktaviani`, Email `vina.oktaviani+{runId}-064@qwertysystem.net`, dan Division sesuai Data valid Create; pilih Group "Area Jakarta"
4. Klik `[Submit]` di Sesi A dan Sesi B hampir bersamaan
5. Tunggu aksi selesai di kedua sesi
6. Verifikasi tepat satu dari dua sesi (sesi pemenang, yaitu sesi yang menampilkan toast sukses) menerima toast sukses "Success, client has been created."
7. Verifikasi popup sesi pemenang tertutup
8. Verifikasi sesi lainnya menampilkan error inline di bawah Company Name: "Company name already exists"
9. Verifikasi popup sesi lainnya tetap terbuka dengan isian dipertahankan
10. Verifikasi sesi lainnya tidak menampilkan toast sukses "Success, client has been created."
11. [Sesi pemenang] Ketik Search `PT Balapan Uji {runId}-064`, tekan Enter
12. Verifikasi List sub-tab Active memuat tepat satu baris "PT Balapan Uji {runId}-064"
13. Verifikasi Group baris tersebut sesuai pilihan sesi pemenang (`Cabang Menteng` bila Sesi A pemenang; `Area Jakarta` bila Sesi B pemenang)
14. [Sesi lainnya] Klik `[✕]` di header popup
15. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
16. Klik `[Leave]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Langkah penghubung (S-03): langkah 5 ("Tunggu aksi selesai" sebelum pindah surface), langkah 11 (Search untuk menemukan baris target, R-16), dan langkah 14 sampai 16 (penutup form dirty pada sesi yang kalah, S-08). Verifikasi "tepat satu baris" memakai nama bersuffix unik (baseline nol).
- Pemenang dibaca dari sesi yang menampilkan toast sukses (Data Uji TC-519); Search langkah 11 dilakukan di sesi pemenang (TC menyebut Sesi A) karena popup sesi yang kalah masih terbuka di atas List.
- Temuan untuk QA:
  - TC-519 bertanda Manual Only (dua sesi paralel); "hampir bersamaan" tidak menyebut jeda maksimum; spec menjalankan kedua klik tanpa jeda yang disengaja.
