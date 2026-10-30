---
id: TC-AC-PP-E2E-004-first-time-create-screening-dan-validasi-v01
title: "First-time Create Privacy Policy: Screening Modal, Validasi V-01 Diblokir, dan Clear Field"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-34
  - TC-AC-PP-36
  - TC-AC-PP-37
  - TC-AC-PP-38
coverage:
  web: automated
---

# First-time Create Privacy Policy: Screening Modal, Validasi V-01 Diblokir, dan Clear Field

## Prerequisites

- Mode: mock. Seluruh API di-mock (dijalankan tim FE sebagai integration test): respons daftar riwayat versi dipaksa 0 versi (Riwayat C). Tidak ada endpoint Publish yang dipanggil karena seluruh submit diblokir validasi client (V-01).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`. Login nyata dengan `AC_TC_PASSWORD` di hook `before` hanya untuk run non-mock; pada run mock sesi disediakan harness. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Dataset Riwayat C (0 versi) lewat mock daftar riwayat versi; tidak ada data yang dibuat.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).
- Kebutuhan mock sesi dan izin: payload sesi dan izin Total Control (capability "Manage privacy policy" Read dan Update) agar row action Edit dan [Create Privacy Policy] tampil.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons daftar riwayat versi 0 versi; kemampuan menempel/mengetik spasi dan Enter di editor rich text.
- Suite berjalan serial (`parallel: false`).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` (dipakai hanya untuk run non-mock).

## Test Steps

### TC-AC-PP-34: Screening Modal state Edit saat [Create Privacy Policy] diklik pada first-time setup

1. Klik menu Settings > Privacy Policy di sidebar
2. Klik [Create Privacy Policy]
3. Verifikasi `Settings > Privacy Policy > Popup Create Privacy Policy` terbuka langsung di state Edit
4. Susuri modal dari atas ke bawah tanpa mengklik apa pun
5. Verifikasi Header: Title modal "Create Privacy Policy"
6. Verifikasi Header: tombol close `[✕]`
7. Verifikasi Body: toolbar format berurutan `H1 | H2 | H3`, `B | I | U`, `• List | 1. List`, `Link`, `Undo | Redo`
8. Verifikasi Body: area editor kosong dengan placeholder "Enter privacy policy content"
9. Verifikasi Footer: `[Clear Field]` (text, primary)
10. Verifikasi Footer: `[Publish New Version]` (Success)
11. Verifikasi Footer: tidak ada tombol `[Cancel]`
12. Verifikasi Footer: tidak ada tombol Close
13. Hover tiap tombol toolbar berurutan dari `H1` sampai `Redo`
14. Verifikasi tooltip dan `aria-label` tombol toolbar berurutan: "Heading 1", "Heading 2", "Heading 3", "Bold", "Italic", "Underline", "Bulleted list", "Numbered list", "Insert link", "Undo", "Redo"

### TC-AC-PP-36: Publish dengan editor kosong diblok client dengan error inline V-01 tanpa membuka dialog

15. Biarkan editor kosong lalu klik [Publish New Version]
16. Verifikasi error inline "Privacy policy content must not be empty" tampil di bawah editor
17. Verifikasi Dialog Publish Confirm tidak terbuka
18. Verifikasi modal tetap terbuka di state Edit
19. Verifikasi tidak ada toast

### TC-AC-PP-37: Publish dengan konten yang hanya berisi whitespace diblok client dengan error inline V-01

20. Ketik 5 spasi pada editor lalu klik [Publish New Version]
21. Verifikasi error inline "Privacy policy content must not be empty" tampil (konten a: 5 spasi, menghasilkan `&nbsp;` di HTML editor)
22. Verifikasi Dialog Publish Confirm tidak terbuka
23. Klik [Clear Field], tekan Enter 3 kali pada editor lalu klik [Publish New Version]
24. Verifikasi error inline "Privacy policy content must not be empty" tampil (konten b: 3 baris kosong)
25. Verifikasi Dialog tidak terbuka
26. Klik [Clear Field], ketik 3 spasi lalu tekan Enter 2 kali lalu klik [Publish New Version]
27. Verifikasi error inline "Privacy policy content must not be empty" tampil (konten c: 3 spasi + 2 baris kosong)
28. Verifikasi Dialog tidak terbuka

### TC-AC-PP-38: Clear Field pada first-time setup mengosongkan editor dan menampilkan kembali placeholder tanpa dialog

29. Klik [Clear Field]
30. Ketik "Draft text" pada editor
31. Klik `[Clear Field]`
32. Verifikasi editor kosong dengan placeholder "Enter privacy policy content"
33. Verifikasi tidak ada dialog konfirmasi
34. Verifikasi modal tetap terbuka di state Edit
35. Verifikasi Title modal tetap "Create Privacy Policy"
36. Klik `[✕]` di header untuk menutup modal (editor kosong, tidak ada dialog)

## Notes

- Mode: mock. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`. Semua TC bertanda FE Test "UI Only" di TC sumber.
- Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan/penggabungan form (S-05, prinsip 6): TC sumber membuka modal baru pada langkah 1 TC-AC-PP-36, TC-AC-PP-37, dan TC-AC-PP-38 ("Klik [Create Privacy Policy]"). Spec memakai satu sesi modal dari TC-AC-PP-34 karena editor belum diubah (identik dengan modal baru) dan jumlah buka form tidak boleh melebihi jumlah kejadian menutup; kasus menutup form ada di spec 005. Langkah 29 mengosongkan editor sebelum TC-AC-PP-38 sehingga state awal sama dengan modal baru.
- Verifikasi langkah 3 (modal Create terbuka langsung di state Edit) diturunkan dari tanda "→" di kolom Langkah Uji TC-AC-PP-34, bukan dari kolom Expected Result; ditambahkan sebagai penanda state sebelum asersi layout (S-03).
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 4, 13 (hover tombol toolbar agar tooltip dan `aria-label` TC-AC-PP-34 d dapat diasersi), langkah 29 dan 36 (Clear Field dan penutupan modal bersih; tidak ada dialog karena editor kosong).
- Temuan untuk QA:
  - TC-AC-PP-34 Expected d (tooltip dan `aria-label` toolbar) tidak punya langkah hover di TC; spec menambahkan langkah hover sebagai penghubung.
  - TC-AC-PP-37 Data Uji (a) menyebut "5 spasi (menghasilkan `&nbsp;` di HTML editor)"; keberadaan `&nbsp;` tidak dapat diasersi dari UI dan tidak diasersi.
  - Tidak ada TC yang menetapkan timing hilangnya error V-01 di antara kasus a, b, dan c (NC-14 hanya diuji di TC-AC-PP-88); langkah `[Clear Field]` menghapus error sebelum konten berikutnya diasersi.
