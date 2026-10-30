---
id: TC-GS-IMPORT-E2E-089-karakter-emoji-pada-employee-id-first-name-dan-last-name-user-login-dan
title: "Karakter emoji pada Employee ID, First Name dan Last Name (User Login dan User Non Login)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-861
  - TC-GS-IMPORT-862
  - TC-GS-IMPORT-863
  - TC-GS-IMPORT-864
coverage:
  web: automated
---

# Karakter emoji pada Employee ID, First Name dan Last Name (User Login dan User Non Login)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import untuk Client C.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Pre-setup Client C (tidak diubah spec ini): User Login `rina.admin.c@example.com` (Activated), Division `Engineering`. Client C tanpa draft pada Sub-Tab User Login dan User Non Login sebelum tiap TC (Kontrak Fixture R1).
- Data Dinamis (berkas fixture uji, D-07; draft tidak di-commit dan dibuang oleh reset; Email bersuffix per run):

  | TC | Sub-Tab | Berkas | Isi |
  |---|---|---|---|
  | 861 | User Login | `user-login-empid-emoji.csv` | header `First Name,Last Name,Email,Division,Position,Employee ID,Access`; 1 baris `Siti`, `Rahmawati`, `siti.emoji.c+{runId}-089@example.com`, `Engineering`, kosong, `EMP😀01`, `Global Settings` |
  | 864 | User Login | `user-login-name-emoji.csv` | berkas User Login standar (D-45); 1 baris `Dewi😀`, `Anggraini`, `dewi.emoji2.c+{runId}-089@example.com`, `Engineering`, kosong, `Global Settings` |
  | 862 | User Non Login | `user-nonlogin-empid-emoji.csv` | header `First Name,Last Name,Email,Division,Position,Employee ID,Represented By`; 1 baris `Agus`, `Pratama`, `agus.emoji.c+{runId}-089@example.com`, `Engineering`, kosong, `EMP😀02`, `rina.admin.c@example.com` |
  | 863 | User Non Login | `user-nonlogin-name-emoji.csv` | header `First Name,Last Name,Email,Division,Represented By`; 1 baris `Dewi😀`, `Anggraini😀`, `dewi.emoji.c+{runId}-089@example.com`, `Engineering`, `rina.admin.c@example.com` |
- Kemampuan teknis: pemilihan berkas berisi emoji pada dialog unggah, pengamatan toast, skrip reset draft per Sub-Tab (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): draft User Login dan User Non Login Client C dibuang lewat skrip reset.

## Test Steps

### User Login

1. Pilih Sub-Tab User Login; reset draft User Login Client C lewat skrip reset, lalu muat ulang halaman
2. Klik `[Upload File]` dan pilih berkas `user-login-empid-emoji.csv` pada file picker
3. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
4. Verifikasi baris 1 berstatus `error`
5. Verifikasi Error Summary Callout memuat "Employee ID contains invalid characters" dengan badge "1 row"
6. Verifikasi Staging Metric Cards: Total Rows 1 (Active), Ready to Import 0, Errors 1, Duplicates 0 (Disabled)
7. Tunggu toast lama hilang otomatis; reset draft User Login Client C lewat skrip reset, lalu muat ulang halaman
8. Klik `[Upload File]` dan pilih berkas `user-login-name-emoji.csv` pada file picker
9. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
10. Verifikasi baris 1 berstatus `pending`
11. Verifikasi baris 1 tanpa border `danger`
12. Verifikasi Error Summary Callout tidak tampil

### User Non Login

13. Tunggu toast lama hilang otomatis; pilih Sub-Tab User Non Login; reset draft User Non Login Client C lewat skrip reset, lalu muat ulang halaman
14. Klik `[Upload File]` dan pilih berkas `user-nonlogin-empid-emoji.csv` pada file picker
15. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
16. Verifikasi baris 1 berstatus `error`
17. Verifikasi Error Summary Callout memuat "Employee ID contains invalid characters" dengan badge "1 row"
18. Tunggu toast lama hilang otomatis; reset draft User Non Login Client C lewat skrip reset, lalu muat ulang halaman
19. Klik `[Upload File]` dan pilih berkas `user-nonlogin-name-emoji.csv` pada file picker
20. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
21. Verifikasi baris 1 berstatus `error`
22. Verifikasi Error Summary Callout memuat "First name contains invalid characters" dengan badge "1 row"
23. Verifikasi Error Summary Callout memuat "Last name contains invalid characters" dengan badge "1 row"
24. Verifikasi urutan pesan pada Error Summary Callout: First Name lebih dulu, lalu Last Name

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan blok ke Sub-Tab; id TC: langkah 1 sampai 6 TC-861, langkah 7 sampai 12 TC-864, langkah 14 sampai 17 TC-862, langkah 18 sampai 24 TC-863.
- Penyimpangan urutan dari TC: TC-864 (Positive, User Login) diletakkan sesudah TC-861 supaya Sub-Tab User Login tidak berpindah dua kali; urutan TC-862 dan TC-863 tetap.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 7, 13, dan 18 (menunggu toast, pemilihan Sub-Tab, reset draft, muat ulang) menjalankan Precondition "Client C tanpa draft Tab X (fixture direset sebelum TC, Kontrak Fixture R1)".
- Asersi "tidak tampil" langkah 12 didahului baris 1 tampil dengan status `pending` (langkah 10) sebagai anchor positif pada surface yang sama.
- Temuan untuk QA:
  - TC-GS-IMPORT-863 Expected b menyebut tiga klausa dalam satu butir (kedua pesan dan urutannya); spec memecahnya menjadi langkah 22, 23, dan 24.
  - TC-GS-IMPORT-862 dan 863: Staging Metric Cards tidak disebut di Expected; tidak diasersi.
  - Post Condition tiap TC (isi draft) tidak punya langkah observasi dan padanan Expected-nya sudah diasersi; tidak diasersi terpisah (S-01).
  - Mekanisme skrip reset draft per Sub-Tab disediakan tim FE/BE (S-13).
