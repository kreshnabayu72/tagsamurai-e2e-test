---
id: TC-AC-RP-E2E-012-screening-role-detail-group-role
title: "Screening Role Detail Group Role: Kolom, Sidebar Group Tree, Exact Match Node, dan Empty State"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-46
  - TC-AC-RP-47
  - TC-AC-RP-48
  - TC-AC-RP-49
coverage:
  web: automated
---

# Screening Role Detail Group Role: Kolom, Sidebar Group Tree, Exact Match Node, dan Empty State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #11 (tree group Principal), #13, #14 (penugasan GM `Fajar Nugroho` dan `Jane Smith` di `Region Jawa`), dan #15 (`Manage distributor`: `John Dohan` `Region A` C/R/U dan `Branch 1` R; `Alex Tan` `Region A` R). Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Data Dinamis: group `Gudang Baru {runId}-012` (Tabel Data Uji Dinamis #2), dibuat tanpa penugasan Group Role dan sesudah seluruh Total Control dan Read Only ditetapkan, sehingga tidak ada baris di Role Detail `Manage distributor` untuk group ini. Group dibuat di hook `before` lewat kemampuan seeding yang disediakan tim FE/BE (membuat group di Settings > Group; mekanismenya tidak didefinisikan di TC) dan dihapus di hook `after`. Nama group bersuffix karena TC tidak mengasersi teks nama literal selain klik node.
- Spec tidak mengubah data Pre-setup; pemulihan baseline automation tidak diperlukan selain cleanup group di atas.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-46: Screening Role Detail Group Role

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
3. Susuri halaman dari atas ke bawah
4. Verifikasi Breadcrumb "Settings > Role & Permission > System > Detail"
5. Verifikasi Page Header menampilkan Title "Manage distributor"
6. Verifikasi Page Header menampilkan deskripsi "This role allows the user to manage distributor organizations within assigned groups through the Distributor menu."
7. Verifikasi Toolbar: Search, Filter, Download, Changelog, "+ Assign"
8. Verifikasi tabel berkolom: Checkbox, Name, Group (sebelum C/R/U/D), Position, Division, C, R, U, D, Actions
9. Verifikasi Sidebar Group Tree tampil di kanan dengan "All Groups" aktif
10. Verifikasi tidak ada section Approval Settings

### TC-AC-RP-47: Satu user di beberapa group tampil per baris dengan CRUD berbeda

11. Ketik Search "John Dohan", tekan Enter
12. Verifikasi tabel menampilkan dua baris `John Dohan`
13. Verifikasi baris `John Dohan` ber-Group `Region A`: C ☑ R ☑ U ☑ D ☐
14. Verifikasi baris `John Dohan` ber-Group `Branch 1`: hanya R ☑
15. Verifikasi Name, Position, dan Division berulang di tiap baris
16. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-RP-48: Klik node sidebar Role Detail Group menyaring exact match

17. Klik node `Region Jawa`
18. Verifikasi tabel menampilkan sedikitnya satu baris
19. Verifikasi tabel hanya menampilkan baris ber-Group `Region Jawa` (termasuk baris Total Control, Read Only, Default User, serta `Fajar Nugroho` dan `Jane Smith` sebagai GM)
20. Verifikasi baris `Jakarta` dan `Surabaya` tidak ikut

### TC-AC-RP-49: Node tanpa penugasan menampilkan empty state Detail Role

21. Klik node `Gudang Baru {runId}-012`
22. Verifikasi tabel menampilkan empty state dengan Title "No users assigned to this role yet." dan Description "Users assigned to this role will appear here."

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE; spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03): langkah 3 (susur halaman sebagai prasyarat asersi) dan langkah 16 (mengosongkan Search dengan klik `(←)` sebagai pengganti frasa "Kosongkan Search", R-16). Search "John Dohan" pada TC-AC-RP-47 adalah langkah TC sumber.
- Verifikasi tabel menampilkan sedikitnya satu baris pada TC-AC-RP-48 adalah pembanding generik untuk asersi universal "hanya baris ber-Group Region Jawa" dan absence baris `Jakarta` dan `Surabaya` (8b butir 2). Tidak ada asersi tambahan atas Expected TC.
- Pembagian TC lintas spec: TC-AC-RP-50 (deskripsi Group Role untuk 6 role) ada di spec 121.
- Temuan untuk QA:
  - TC-AC-RP-49 Precondition d ("Group `Gudang Baru` dibuat ... setelah seluruh Total Control dan Read Only ditetapkan") tidak menjelaskan mengapa Total Control dan Read Only tidak diproyeksikan sebagai baris di group baru, sedangkan TC-AC-RP-48 menampilkan baris Total Control dan Read Only pada `Region Jawa`; mekanisme pembuatan group dan penetapan itu tidak didefinisikan di TC.
  - TC-AC-RP-48 menyebut "baris Total Control, Read Only, Default User" ber-Group `Region Jawa` tanpa merinci nama dan jumlahnya; asersi memakai deskripsi TC.
