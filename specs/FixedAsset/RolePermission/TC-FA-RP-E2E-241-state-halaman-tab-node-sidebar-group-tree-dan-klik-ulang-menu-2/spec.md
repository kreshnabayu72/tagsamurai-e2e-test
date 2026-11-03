---
id: TC-FA-RP-E2E-241-state-halaman-tab-node-sidebar-group-tree-dan-klik-ulang-menu-2
title: "State halaman: tab, node Sidebar Group Tree, dan klik ulang menu (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-791
  - TC-FA-RP-793
  - TC-FA-RP-1029
coverage:
  web: automated
---

# State halaman: tab, node Sidebar Group Tree, dan klik ulang menu (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #18 (pohon group), #19 (seed Role Transaksi), #38 (Tab Group Manager terisi), #39 (Detail Role `Manage files` terisi: pada `Data Center` Ahmad Fauzi dan Dimas Pranata). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Muat ulang halaman (F5), klik Breadcrumb, dan klik Back; pembaca berkas unduhan CSV (baris dan kolom), disediakan tim FE/BE.
- State yang diubah dan pemulihannya: Tidak ada state backend yang diubah; Search yang diketik hanya state UI.
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-791: Klik ulang menu Settings > Role & Permission mereset state ke default

1. Klik Tab `Group Manager`
2. Klik node `Data Center`
3. Ketik Search `kevin`, tekan Enter
4. Klik menu Role & Permission di sidebar
5. Verifikasi halaman dibuka pada Tab `Total Control` (default)
6. Klik Tab `Group Manager` untuk mengamati state tab yang tadi diubah
7. Verifikasi Search Tab `Group Manager` kembali ke default (kosong)
8. Verifikasi Filter Tab `Group Manager` kembali ke default
9. Verifikasi Sort Tab `Group Manager` kembali ke default
10. Verifikasi paginasi Tab `Group Manager` kembali ke default (halaman 1)
11. Verifikasi node Sidebar Group Tree Tab `Group Manager` kembali ke default

### TC-FA-RP-793: Download Detail Role Group Role mengikuti node terpilih bersama Search dan Filter

12. Klik Tab `System`
13. Buka Detail Role `Manage files`
14. Klik node `Data Center`
15. Klik ikon Download
16. Klik `Download as CSV`
17. Verifikasi berkas memuat baris Ahmad Fauzi dan Dimas Pranata (penugasan langsung pada node `Data Center`)
18. Verifikasi berkas tidak memuat baris selain penugasan langsung pada node `Data Center`

### TC-FA-RP-1029: Tab Transaction Role: sub-tab awal Borrowing & Assignment, sub-tab aktif dan node group dipertahankan setelah F5 dan Back dari Detail Role

19. Klik segmen `System` pada Breadcrumb lalu klik Tab `Transaction Role`
20. Klik node `IT Infrastructure`
21. Verifikasi sub-tab `Borrowing & Assignment` aktif saat pertama masuk
22. Klik sub-tab `Transfer`
23. Muat ulang halaman (F5)
24. Verifikasi sub-tab `Transfer` tetap aktif
25. Verifikasi Tab `Transaction Role` tetap aktif
26. Verifikasi node `IT Infrastructure` tetap aktif
27. Klik Tab `System`
28. Buka Detail Role `Manage files`
29. Klik Back
30. Klik Tab `Transaction Role` kembali
31. Verifikasi Tab `Transaction Role` aktif
32. Verifikasi sub-tab `Transfer` dipertahankan
33. Verifikasi node `IT Infrastructure` dipertahankan

## Notes

- Asersi isi berkas Download (baris yang dibandingkan dengan layar atau modal) tetap berada di spec fungsional ini dan tidak dipecah ke spec kelas f (konvensi bagian 3 butir 13f, [KEPUTUSAN 2026-11-02]).
- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 33 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 6, 12, 19. Akun aktor pertama sudah login di hook `before` (S-07).
- Temuan untuk QA:
  - TC-FA-RP-791 Expected menyebut state Search, Filter, Sort, paginasi, dan node "kembali ke default" tanpa menyebut tab dan nama node default; spec mengamatinya di Tab `Group Manager` (tempat state diubah) dan tidak menyebut nama node default.
  - TC-FA-RP-793 judul menyebut Search dan Filter, tetapi langkah hanya memilih node dan Download; spec mengikuti langkah dan Expected.
  - TC-FA-RP-1029 langkah 5 menyebut "klik Back" tanpa menyebut elemen (tombol Back UI atau Breadcrumb); spec menulis `Klik Back` apa adanya.
