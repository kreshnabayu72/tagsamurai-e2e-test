---
id: TC-FA-RP-E2E-234-isi-berkas-download-csv-dan-xlsx-2
title: Isi berkas Download CSV dan XLSX (2/2)
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-669
  - TC-FA-RP-753
  - TC-FA-RP-1024
coverage:
  web: automated
---

# Isi berkas Download CSV dan XLSX (2/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #39 (Detail Role Group Role `Manage files` terisi enam baris; Ahmad Fauzi dengan Read dan Delete aktif, Create dan Update tidak berlaku), #36 (Tab Total Control terisi sembilan baris; Rina Wulandari dengan Modified By `Admin U`, Admin Utama dengan Modified By `System`), dan #42 (Changelog Tab Total Control, enam entri seed, Field `Access Level`; urutan relatif entri seed pada User Name ascending: Ahmad Fauzi, Budi Santoso (Remove lalu Assign), Fitri Handayani, Maya Anggraeni, Rina Wulandari). Pre-setup #18, #24, dan #34 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Seeding enam entri seed #42 dijamin fixture backend yang disediakan tim FE/BE di hook `before`. Changelog adalah audit trail permanen yang tidak dipulihkan: entri lain dapat ada di antara entri seed, sehingga entri seed dikenali lewat kombinasi Action, User Name, Old Value, New Value, dan Modified By seperti pada Pre-setup #42.
- Kemampuan teknis (kelas binary buffer): pembaca isi berkas unduhan CSV dan XLSX (encoding, BOM, escape, sheet, nilai sel, dan urutan baris); disediakan tim FE/BE.
- State global: Date Format General Settings diubah pada langkah 26 (kemampuan baca dan ubah General Settings disediakan tim FE/BE); nilai awal dicatat di hook `before`, nilai format lain dirujuk lewat `Fixture.fixedAssetRolePermission.dateFormatLain`, dan nilai awal dipulihkan pada langkah 35 serta di hook `after`.

## Test Steps

### Download Detail Role: kolom CRUD Yes atau No (TC 669)

1. Klik Tab `System`.
2. Klik Role Name `Manage files` pada section Group Role.
3. Klik `All Groups` di Sidebar Group Tree.
4. Klik ikon Download, lalu klik `Download as CSV`.
5. Verifikasi pada baris Ahmad Fauzi kolom Read bernilai `Yes` dan kolom Delete bernilai `Yes`.
6. Verifikasi pada baris Ahmad Fauzi kolom Create dan Update (tidak berlaku pada `Manage files`) bernilai `-`.

### Download Modal Changelog: aturan teknis CSV dan XLSX (TC 753)

7. Buka halaman Role & Permission lewat menu sidebar (kembali ke Tab `Total Control`).
8. Klik ikon Changelog pada toolbar.
9. Klik header kolom User Name sekali (User Name ascending).
10. Klik ikon Download, lalu klik `Download as CSV`.
11. Klik ikon Download, lalu klik `Download as XLSX`.
12. Verifikasi CSV berenkode UTF-8 dengan BOM.
13. Verifikasi nilai CSV yang berisi koma atau tanda kutip di-escape.
14. Verifikasi XLSX memuat satu sheet bernama `Sheet1`.
15. Verifikasi sel kosong ditulis `-` pada CSV dan XLSX.
16. Verifikasi urutan baris CSV mengikuti Sort aktif (User Name ascending), dengan urutan relatif entri seed Pre-setup #42 (entri lain dari audit trail permanen dapat berada di antaranya): Ahmad Fauzi, Budi Santoso (Remove lalu Assign; tie-breaker default sort Date descending), Fitri Handayani, Maya Anggraeni, Rina Wulandari.
17. Verifikasi urutan relatif entri seed pada baris XLSX sama dengan urutan CSV pada langkah 16.
18. Tutup modal Changelog.

### Download Tab Total Control: Modified By dan Last Updated mengikuti Date Format (TC 1024)

19. Catat teks sel Last Updated baris Rina Wulandari di layar.
20. Arahkan kursor ke sel Modified By baris Rina Wulandari.
21. Verifikasi tooltip nama lengkap `Admin Utama` (layar menampilkan `Admin U`).
22. Klik ikon Download, lalu klik `Download as CSV`.
23. Verifikasi pada baris Rina Wulandari kolom Modified By berisi `Admin Utama` (nama lengkap).
24. Verifikasi pada baris Rina Wulandari kolom Last Updated sama dengan teks tanggal yang dicatat pada langkah 19.
25. Verifikasi pada baris Admin Utama kolom Modified By berisi `System`.
26. Ubah Date Format di General Settings ke format lain (kemampuan disediakan tim FE/BE).
27. Muat ulang halaman (F5).
28. Catat teks sel Last Updated baris Rina Wulandari di layar.
29. Klik ikon Download, lalu klik `Download as XLSX`.
30. Verifikasi kolom Last Updated pada berkas XLSX mengikuti Date Format yang baru dan sama dengan teks tanggal yang dicatat pada langkah 28.
31. Klik ikon Filter.
32. Verifikasi field `Modified By` adalah multi-select searchable `All users`.
33. Verifikasi opsi field `Modified By` dari nilai unik data tabel: `Admin Utama`, `Prasetyo Hadi`, `Siti Rahmawati`, `System`.
34. Klik ikon Filter untuk menutup panel.
35. Pulihkan Date Format General Settings ke nilai awal (kemampuan disediakan tim FE/BE).

## Notes

- Langkah penghubung (S-03): langkah 7 (kembali ke halaman awal setelah Detail Role), 18 (menutup modal), 19 (mencatat teks layar sebagai pembanding langkah 24), 26 dan 27 (menggeser state sesuai TC), 28 (mencatat teks layar sebagai pembanding langkah 30), 34, dan 35 (memulihkan Date Format, sesuai Post Condition TC 1024 yang mendefinisikan pemulihan).
- Kelas f (binary buffer): spec hanya memuat TC yang mengasersi isi berkas.
- Temuan untuk QA:
  - TC 1024 butir b ("kolom Last Updated sama dengan teks tanggal di layar") tidak menyebut cara mencatat teks layar; spec menambah langkah pencatatan 19 dan 28.
  - TC 1024 butir d merujuk TC-FA-RP-483 untuk opsi `Modified By`; spec memakai daftar opsi yang tertulis pada TC 1024.
  - Data Changelog #42 tidak memuat nilai yang berisi koma atau tanda kutip, sehingga asersi escape pada langkah 13 hanya terasersi bila fixture memuatnya.
  - TC 669 langkah 4 menyebut baris Ahmad Fauzi pada berkas CSV tanpa menyebut kolom lain; spec mengasersi hanya kolom Create, Read, Update, dan Delete.
  - `caseType` spec ini `Edge` karena seluruh TC sumber bertipe Edge Case.
