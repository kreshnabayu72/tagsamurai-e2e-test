---
id: TC-FA-RP-E2E-233-isi-berkas-download-csv-dan-xlsx-1
title: Isi berkas Download CSV dan XLSX (1/2)
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-525
  - TC-FA-RP-573
  - TC-FA-RP-667
coverage:
  web: automated
---

# Isi berkas Download CSV dan XLSX (1/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris; Rina Wulandari dengan Position `Operations Manager, Region 1` dan Division `Asset Management "North"`), #38 (Tab Group Manager terisi enam baris), dan #39 (Detail Role Group Role `Manage files` terisi enam baris). Pre-setup #37 dan #18 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Spec ini tidak mengubah data; Pre-setup di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis (kelas binary buffer): pembaca isi berkas unduhan CSV dan XLSX (encoding, BOM, escape, sheet, nilai sel, dan urutan baris); disediakan tim FE/BE.

## Test Steps

### Download Tab Total Control (TC 525)

1. Klik header kolom Position sekali (Position ascending).
2. Klik ikon Download, lalu klik `Download as CSV`.
3. Klik ikon Download, lalu klik `Download as XLSX`.
4. Verifikasi CSV berenkode UTF-8 dengan BOM.
5. Verifikasi nilai CSV yang berisi koma atau tanda kutip di-escape (Position `Operations Manager, Region 1` dan Division `Asset Management "North"` pada baris Rina Wulandari).
6. Verifikasi XLSX memuat satu sheet bernama `Sheet1`.
7. Verifikasi sel kosong ditulis `-` pada CSV dan XLSX.
8. Verifikasi urutan baris CSV mengikuti Sort aktif (Position ascending): Ahmad Fauzi, Eka Saputra, Fitri Handayani, Siti Rahmawati (sama-sama `Finance Officer`; tie-breaker default sort Name A-Z), Rudi Hartono, Siti Rahayu, Rina Wulandari, Admin Utama, Budi Santoso.
9. Verifikasi urutan baris XLSX sama dengan urutan CSV pada langkah 8.
10. Klik header kolom Position dua kali hingga sort kembali ke default.

### Download Tab Group Manager (TC 573)

11. Klik Tab `Group Manager`.
12. Klik header kolom Group sekali (Group ascending).
13. Klik ikon Download, lalu klik `Download as CSV`.
14. Klik ikon Download, lalu klik `Download as XLSX`.
15. Verifikasi CSV berenkode UTF-8 dengan BOM.
16. Verifikasi nilai CSV yang berisi koma atau tanda kutip di-escape.
17. Verifikasi XLSX memuat satu sheet bernama `Sheet1`.
18. Verifikasi sel kosong ditulis `-` pada CSV dan XLSX.
19. Verifikasi urutan baris CSV mengikuti Sort aktif (Group ascending berdasarkan nama group): Kevin Susanto (`Data Center`), Lina Marlina (`Head Office`), Kevin Susanto (`Helpdesk`), Cahyo Aji (`International Operations Distribution Center`), Fajar Nugroho (`IT Infrastructure`), Dimas Pranata (`Rack A1`).
20. Verifikasi urutan baris XLSX sama dengan urutan CSV pada langkah 19.
21. Klik header kolom Group dua kali hingga sort kembali ke default.

### Download Detail Role (TC 667)

22. Klik Tab `System`.
23. Klik Role Name `Manage files` pada section Group Role.
24. Klik `All Groups` di Sidebar Group Tree.
25. Klik header kolom Position sekali (Position ascending).
26. Klik ikon Download, lalu klik `Download as CSV`.
27. Klik ikon Download, lalu klik `Download as XLSX`.
28. Verifikasi CSV berenkode UTF-8 dengan BOM.
29. Verifikasi nilai CSV yang berisi koma atau tanda kutip di-escape.
30. Verifikasi XLSX memuat satu sheet bernama `Sheet1`.
31. Verifikasi sel kosong ditulis `-` pada CSV dan XLSX.
32. Verifikasi urutan baris CSV mengikuti Sort aktif (Position ascending): Ahmad Fauzi (Asset Custodian), Fitri Handayani (Finance Officer), Citra Lestari (HR Officer), Dimas Pranata (IT Support), Endah Susanti (Procurement Officer), Budi Santoso (Warehouse Staff).
33. Verifikasi urutan baris XLSX sama dengan urutan CSV pada langkah 32.

## Notes

- Langkah penghubung (S-03): langkah 10 dan 21 (mengembalikan sort ke default antar TC, sesuai S-09), 11 dan 22 sampai 24 (berpindah tab dan memilih surface sesuai Precondition TC; Tab `Total Control` dibuka hook `beforeEach` suite sehingga langkah TC `Klik Tab Total Control` tidak diulang).
- Kelas f (binary buffer): spec hanya memuat TC yang mengasersi isi berkas.
- Temuan untuk QA:
  - Data Pre-setup #38 dan #39 tidak memuat nilai yang berisi koma atau tanda kutip, sehingga asersi escape pada langkah 16 dan 29 hanya terasersi pada data #36 (langkah 5).
  - TC 525, 573, dan 667 mengasersi urutan file tanpa menyebut urutan XLSX terpisah; spec mengasersi urutan XLSX sama dengan CSV (Expected "urutan baris berkas").
  - TC 667 menyebut precondition `User berada di ... System`; spec menambah langkah 22 karena halaman awal adalah Tab `Total Control`.
  - `caseType` spec ini `Edge` karena seluruh TC sumber bertipe Edge Case.
