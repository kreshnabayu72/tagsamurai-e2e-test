---
id: TC-FA-PREF-E2E-086-dua-admin-menyimpan-journal-grouping-bersamaan-last-write-wins-dan-tiap-save-dicatat
title: "Dua Admin Menyimpan Journal Grouping Bersamaan: Last-Write-Wins dan Tiap Save Dicatat"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-287
sourceRules: ["T-01", "F-FAPREF-01.k7a", "FAPREF-LOGIC-09c", "F-FAPREF-01.k7b", "L-02e", "L-02f"]
smoke: []
dependsOn: []
trace:
  "T-01": [5, 8]
  "F-FAPREF-01.k7a": [12, 13]
  "FAPREF-LOGIC-09c": [12, 13]
  "F-FAPREF-01.k7b": [15, 20]
  "L-02e": [15, 16, 17, 20]
  "L-02f": [16, 17, 20]
coverage:
  web: automated
---

# Dua Admin Menyimpan Journal Grouping Bersamaan: Last-Write-Wins dan Tiap Save Dicatat

## Prerequisites

- Mode: FE+BE.
- Kelas harness: c (dua sesi UI paralel, dua admin).
- Akun aktor: Admin A = Total Control (Pre-setup PC-8: Rina Anggraini) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Admin B = Manage accounting - Read + Update (Pre-setup PC-8: Budi Santoso, tampil "Budi S"); email akun ini tidak tertulis di Pre-setup TC (disediakan tim FE); password `Spectra.env.FA_MARU_PASSWORD`. Env var `FA_TC_PASSWORD` (Admin A) dan `FA_MARU_PASSWORD` (Admin B) belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE; satu nama per akun, skema `FA_<ROLE>_PASSWORD` mengikuti spec 077 dan 078.
- Login Admin A di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Sesi Admin B dibuka pada langkah 1 (konteks browser kedua) dan ditutup pada langkah 21; hook `after` menutup sesi itu bila spec gagal di tengah dan mengembalikan sesi ke akun default suite.
- Data Pre-setup: Preferences nilai awal PB-1 dengan Journal Grouping tersimpan "Group"; akun Chart of Accounts PB-2; Changelog Preferences berisi 1 entri Create. Admin A dan Admin B sama-sama membuka tab Preferences dengan nilai Journal Grouping "Group" (langkah 1 dan hook `beforeEach`). Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API).
- Kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan): jumlah baris Changelog Preferences, dibaca sebelum aksi sebagai baseline (bagian 8b butir 10, S-12).
- State yang diubah spec: Journal Grouping dan Changelog Preferences (entri audit trail permanen tidak dapat dihapus). Langkah 22 memulihkan Journal Grouping ke "Group" lewat seed; hook `after` menjalankan pemulihan yang sama.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) untuk Admin A dan Admin B.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka konteks browser kedua, login sebagai Admin B (Manage accounting - Read + Update), lalu buka Settings > Accounting > Preferences
2. Catat jumlah baris Changelog Preferences (baseline)
3. Sesi Admin A: centang opsi "Category" pada MultiSelect Journal Grouping
4. Sesi Admin A: klik [Save changes]
5. Sesi Admin A: verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
6. Sesi Admin B: centang opsi "Asset Class" pada MultiSelect Journal Grouping
7. Sesi Admin B: klik [Save changes]
8. Sesi Admin B: verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
9. Tunggu aksi selesai
10. Sesi Admin A: muat ulang tab Preferences dengan F5
11. Sesi Admin B: muat ulang tab Preferences dengan F5
12. Sesi Admin A: verifikasi MultiSelect Journal Grouping menampilkan chip "Group" dan "Asset Class"
13. Sesi Admin B: verifikasi MultiSelect Journal Grouping menampilkan chip "Group" dan "Asset Class"
14. Sesi Admin A: klik ikon View history
15. Sesi Admin A: verifikasi jumlah baris Changelog bertambah 2 dari baseline langkah 2
16. Sesi Admin A: verifikasi satu baris Field Journal Grouping dengan New Value "Group, Category" pada dua baris teratas
17. Sesi Admin A: verifikasi satu baris Field Journal Grouping dengan New Value "Group, Asset Class" pada dua baris teratas
18. Sesi Admin A: klik ikon [✕] di header modal Changelog
19. Sesi Admin B: klik ikon View history
20. Sesi Admin B: verifikasi dua baris teratas memuat Field Journal Grouping dengan New Value "Group, Category" dan "Group, Asset Class"
21. Sesi Admin B: klik ikon [✕] di header modal Changelog, lalu tutup konteks browser kedua
22. Pulihkan Journal Grouping ke "Group" lewat seed hingga tersimpan

## Notes

- Langkah penghubung (S-03, S-09): langkah 1 (membuka sesi Admin B), langkah 9 (menunggu kedua Save selesai sebelum muat ulang), langkah 18 dan 21 (menutup modal dan sesi kedua), langkah 22 (memulihkan Journal Grouping). Layar Preferences Admin A dibuka hook `beforeEach` suite.
- Sesi UI kedua dipakai karena hasil di sesi Admin B diasersi (toast pada langkah 8 dan nilai pada langkah 13 dan 20); karena itu spec berkelas c dan Admin B tidak diperlakukan sebagai pelaku API (bagian 3 prinsip 13, P-2).
- Cara baca Changelog (S-12, S-14): jumlah baris dibaca sebelum Save (langkah 2) dan selisihnya diverifikasi pada langkah 15 sebelum isi dibaca; kedua entri baru dapat jatuh dalam menit yang sama sehingga langkah 16, 17, dan 20 mengasersi himpunan dua baris teratas tanpa mengandalkan urutan di antaranya.
- Temuan untuk QA:
  - TC-FA-PREF-287 berstatus "Manual Only - (d) dua sesi pengguna paralel"; spec tetap ditulis lengkap sebagai spec kelas c dan kemampuan dua konteks browser dicatat di Prerequisites (bagian 2).
  - TC-FA-PREF-287 Expected a menyebut "tampil di kanan bawah layar tampil" (kalimat rancu); spec mengasersi toast tampil di kanan bawah layar pada tiap sesi.
  - TC-FA-PREF-287 Expected b menyebut chip "Group" dan "Asset Class" untuk Admin A dan Admin B bersama ("Admin A dan Admin B: muat ulang") dan Expected c menyebut modal Changelog tanpa menyebut sesi; spec mengasersi keduanya pada kedua sesi.
  - Post Condition TC-FA-PREF-287 butir b ("Tiap Save yang berhasil menulis entri log sendiri") dicakup oleh Expected c.
  - TC-FA-PREF-287 tidak menyebut surface log selain modal Changelog; System Log dan Activity Log tidak diasersi.
