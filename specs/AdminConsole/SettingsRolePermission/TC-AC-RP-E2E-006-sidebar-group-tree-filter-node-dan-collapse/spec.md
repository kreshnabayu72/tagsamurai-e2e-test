---
id: TC-AC-RP-E2E-006-sidebar-group-tree-filter-node-dan-collapse
title: "Sidebar Group Tree: Filter Node, Node Aktif, Collapse, dan Eksklusi Pemegang Tingkat Akses"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-22
  - TC-AC-RP-23
  - TC-AC-RP-24
  - TC-AC-RP-25
  - TC-AC-RP-26
coverage:
  web: automated
---

# Sidebar Group Tree: Filter Node, Node Aktif, Collapse, dan Eksklusi Pemegang Tingkat Akses

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua (ganti akun eksplisit pada langkah 20): Default User Principal `defaultUserRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Bambang Hartono`), password dari `Spectra.env.AC_RP_DU_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`), #13 (pemegang tingkat akses termasuk `Bambang Hartono`), dan #14 (penugasan GM: `Fajar Nugroho` di `Region Jawa` dan `Sumatera`; `Jane Smith` di `Region Jawa`). Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Spec read-only: tidak membuat, mengubah, atau menghapus data; aksi `Remove` tidak dijalankan. Tidak ada data Dinamis, seeding, atau suffix `{runId}`. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` dan `AC_RP_DU_PASSWORD` adalah nama baru; keduanya harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-22: Klik node menyaring ke assignment GM langsung pada group itu saja

1. Klik tab `Group Manager`
2. Klik node `Region Jawa` pada Sidebar Group Tree
3. Verifikasi node `Region Jawa` di-highlight
4. Verifikasi tabel hanya menampilkan baris `Fajar Nugroho` — `Region Jawa` dan `Jane Smith` — `Region Jawa`, dan baris `Fajar Nugroho` — `Sumatera` tidak tampil
5. Verifikasi kolom Group tetap tampil

### TC-AC-RP-23: Node tanpa GM langsung tampil kosong walau ancestor punya GM

6. Klik node `Jakarta` (anak `Region Jawa`)
7. Verifikasi tabel menampilkan empty state dengan Title "No users assigned to this role yet." dan Description "Users assigned to this role will appear here."
8. Verifikasi tidak ada proyeksi baris inherited `Fajar Nugroho`

### TC-AC-RP-24: Klik node aktif lagi tidak men-deselect

9. Klik node `Sumatera`
10. Klik node `Sumatera` sekali lagi
11. Verifikasi `Sumatera` tetap aktif setelah klik kedua
12. Verifikasi selalu ada tepat satu node aktif (single-select, bukan toggle)
13. Klik node "All Groups"
14. Verifikasi tabel mengembalikan seluruh 3 baris

### TC-AC-RP-25: Sidebar Group Tree dapat di-collapse

15. Klik kontrol collapse pada panel Sidebar Group Tree
16. Verifikasi panel sidebar mengecil
17. Klik kontrol expand
18. Verifikasi panel sidebar terbuka kembali
19. Verifikasi node aktif tidak berubah

### TC-AC-RP-26: Default User dan pemegang tingkat akses tidak pernah muncul di Tab Group Manager

20. Logout dari akun `Siti Nurhaliza`
21. Login sebagai `Bambang Hartono` (Default User) dengan password dari `Spectra.env.AC_RP_DU_PASSWORD`
22. Buka halaman `Settings > Role & Permission` lewat menu Settings di sidebar
23. Klik tab `Group Manager`
24. Verifikasi tabel Tab Group Manager menampilkan sedikitnya satu baris
25. Ketik Search "Bambang", tekan Enter
26. Verifikasi tabel menampilkan "No results found"
27. Verifikasi tidak ada baris Default User, Total Control, atau Read Only di Tab Group Manager
28. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
29. Klik `⋯` pada baris `Fajar Nugroho` — `Region Jawa`
30. Verifikasi overlay baris `Fajar Nugroho` memuat `Remove` enabled
31. Tutup overlay row action

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE; spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Ganti akun eksplisit pada langkah 20 karena TC-AC-RP-26 mensyaratkan aktor Default User sedangkan TC-AC-RP-22 sampai TC-AC-RP-25 mensyaratkan Total Control; TC-AC-RP-26 ditaruh di akhir spec agar ganti akun hanya sekali (S-10). Langkah login dan pembukaan halaman sesudahnya adalah langkah penghubung ganti akun (S-07).
- Langkah penghubung tanpa awalan Verifikasi (S-03): langkah 31 menutup overlay row action, dan klik `(←)` pada Search sebelumnya mengosongkan Search sebagai pengganti frasa "Kosongkan Search" (R-16, 8b butir 9). Search "Bambang" pada TC-AC-RP-26 adalah langkah TC sumber.
- Klausa "hanya" pada langkah 4 mengasersi dua baris `Region Jawa` tampil dan baris `Fajar Nugroho` — `Sumatera` tidak tampil; baris itu adalah pembanding yang dijamin ada oleh Pre-setup #14 (8b butir 2).
- Verifikasi tabel Tab Group Manager menampilkan sedikitnya satu baris (langkah 24) adalah anchor positif untuk absence baris Default User, Total Control, dan Read Only (8b butir 2); "No results found" dari Search juga menjadi anchor yang sah.
- Urutan TC-AC-RP-22 sampai TC-AC-RP-25 mengikuti TC sumber; node aktif dibawa antar TC (Region Jawa, Jakarta, Sumatera) dan dikembalikan ke "All Groups" pada TC-AC-RP-24 sebelum TC-AC-RP-25 (S-09).
- Temuan untuk QA:
  - TC-AC-RP-23 Expected menyebut empty state tanpa Illustration pada deskripsi, berbeda dengan TC-AC-RP-60 yang menyebut Illustration; asersi mengikuti Title dan Description saja.
  - TC-AC-RP-26 Langkah Uji "Kosongkan Search" tidak menyatakan aksi; spec memakai klik `(←)` pada kotak Search (konvensi 8b butir 9).
