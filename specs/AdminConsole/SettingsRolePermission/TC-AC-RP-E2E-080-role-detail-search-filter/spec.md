---
id: TC-AC-RP-E2E-080-role-detail-search-filter
title: "Role Detail: Search Global Role dan Group Role, Filter Panel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-276
  - TC-AC-RP-277
  - TC-AC-RP-278
coverage:
  web: automated
---

# Role Detail: Search Global Role dan Group Role, Filter Panel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Spec ini tidak menulis data Pre-setup; tidak ada record bersuffix `+{runId}-NNN` yang dibuat.
- Role Detail Global Role `Manage device master data` memuat user ber-Position Staff `Jane Smith`, `John Dohan`, `Maya Putri`, `Rina Wijaya`, dan `Sarah Kim` serta user ber-Division Operations; Role Detail Group Role `Manage distributor` memuat penugasan pada group `Branch 1` (Pre-setup #11, #15).

## Test Steps

### TC-AC-RP-276: Search Role Detail mencakup Name, Position, Division

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
3. Klik ikon Search
4. Verifikasi placeholder kotak Search "Search name..."
5. Ketik Search `staff`, tekan Enter
6. Verifikasi baris dengan Position Staff tampil (`Jane Smith`, `John Dohan`, `Maya Putri`, `Rina Wijaya`, `Sarah Kim`)

### TC-AC-RP-278: Filter Panel Role Detail

7. Klik `(←)` pada kotak Search
8. Klik ikon Filter
9. Verifikasi Filter Panel memuat field Position dan Division
10. Pilih Division `Operations`
11. Klik `[Apply]`
12. Verifikasi baris ber-Division Operations tampil
13. Verifikasi tidak ada baris selain ber-Division Operations
14. Klik segmen "System" pada Breadcrumb
15. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
16. Klik ikon Filter
17. Verifikasi Filter Panel Detail Group Role memuat field Position dan Division
18. Verifikasi Filter Panel Detail Group Role tidak memuat field Group

### TC-AC-RP-277: Search Role Detail Group Role mencakup kolom Group

19. Ketik Search `branch`, tekan Enter
20. Verifikasi baris ber-Group `Branch 1` tampil
21. Verifikasi tidak ada baris selain ber-Group `Branch 1`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Penyimpangan urutan: TC-AC-RP-278 dijalankan sebelum TC-AC-RP-277 karena TC-AC-RP-278 Expected a menyebut Detail Group Role, sehingga halaman Role Detail `Manage distributor` dibuka di dalam TC-AC-RP-278 dan TC-AC-RP-277 memakainya langsung tanpa membuka ulang.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 7 mengosongkan Search; langkah 14 kembali ke Tab System untuk membuka Role Detail Group Role (S-09).
- Pada TC-AC-RP-278 Expected a (tidak ada field Group pada Detail Group Role), langkah TC hanya membuka Role Detail Global Role `Manage device master data`; langkah membuka Detail Group Role `Manage distributor` dan membuka Filter Panel-nya ditambahkan agar klausa itu dapat diamati (S-03).
- Klausa "(plus curated bila aktif)" pada Expected TC-AC-RP-278 tidak diasersi karena kolom curated tidak diaktifkan.
- Temuan untuk QA:
  - TC-AC-RP-278 Expected a menyebut Detail Group Role tetapi Langkah Uji memakai Global Role `Manage device master data`.
  - TC tidak menyatakan apakah Filter Panel tetap terbuka setelah `[Apply]`.
