---
id: TC-FA-SU-E2E-003-sidebar-group-tree-filter-user-list-per-node-dan-state-preservation
title: "Sidebar Group Tree: Filter User List per Node dan State Preservation"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-7
  - TC-FA-SU-8
coverage:
  web: automated
---

# Sidebar Group Tree: Filter User List per Node dan State Preservation

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md`.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` dengan 25 pengguna (#20) dan pohon grup (#21). Nilai nama pengguna dan grup dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis: tab browser kedua dalam sesi akun aktor yang sama (langkah 40 sampai 45, dipakai hanya untuk mengamati state awal tab baru); muat ulang halaman (F5, tidak ada form terbuka sehingga tidak ada dialog `beforeunload`).
- State global: tidak ada yang diubah selain state tabel (Search, Filter, Sort, node) yang dipulihkan langkah 35 sampai 39 dan oleh klik ulang menu sidebar. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-7: Klik node Sidebar Group Tree memfilter User List sesuai scope node

1. Verifikasi node `All Groups` aktif dan halaman 1 User List berisi 10 baris
2. Klik halaman 2 pada pagination
3. Verifikasi halaman 2 berisi 10 baris
4. Klik halaman 3 pada pagination
5. Verifikasi halaman 3 berisi 5 baris sehingga node `All Groups` menampilkan 25 pengguna
6. Klik node `Finance & Accounting`
7. Verifikasi halaman 1 berisi Ahmad Dahlan, Budi Santoso, Citra Lestari, Gita Permata, Lina Marlina, Nanda Pratama, Oscar Pranata, Putri Anggraeni, Sinta Dewi, Teguh Prakoso
8. Klik halaman 2 pada pagination
9. Verifikasi halaman 2 berisi Umar Faruq dan Wawan Setiawan sehingga node `Finance & Accounting` menampilkan 12 pengguna
10. Klik node `Accounts Payable`
11. Verifikasi User List berisi Ahmad Dahlan, Citra Lestari, Lina Marlina, Oscar Pranata, Putri Anggraeni
12. Klik node `Logistics Warehouse`
13. Verifikasi User List berisi Ahmad Dahlan, Citra Lestari, Lina Marlina, Wawan Setiawan
14. Verifikasi node `Logistics Warehouse` di-highlight sebagai node aktif
15. Verifikasi Doni Prasetyo (Home Group Logistics Warehouse) tidak muncul di User List node `Logistics Warehouse`
16. Klik node `Logistics Warehouse` yang aktif sekali lagi
17. Verifikasi pilihan node dibatalkan (tidak ada node di-highlight selain `All Groups`)
18. Verifikasi tabel kembali menampilkan semua pengguna (pagination memuat 3 halaman)

### TC-FA-SU-8: State preservation User List: Back dari Detail, refresh, dan klik ulang menu sidebar

19. Ketik Search `Budi`, tekan Enter
20. Terapkan Filter Status `Active`
21. Klik header kolom Email untuk mengurutkan
22. Klik node `Finance & Accounting`
23. Klik nama `Budi Santoso`
24. Klik segmen Breadcrumb `User`
25. Verifikasi Search `Budi` terisi kembali
26. Verifikasi Filter Status `Active` aktif kembali
27. Verifikasi Sort Email aktif kembali
28. Verifikasi page size tetap 10
29. Verifikasi node `Finance & Accounting` aktif kembali
30. Verifikasi hasil irisan Search, Filter, dan node berisi Budi Santoso dan Putri Anggraeni (2 baris, hanya halaman 1)
31. Tekan F5
32. Verifikasi Search `Budi`, Filter Status `Active`, Sort Email, dan node `Finance & Accounting` tetap sama setelah F5
33. Verifikasi hasil irisan tetap Budi Santoso dan Putri Anggraeni (2 baris)
34. Klik menu Settings > User pada sidebar navigasi
35. Verifikasi Search kosong
36. Verifikasi Filter tidak aktif
37. Verifikasi Sort kembali ke default
38. Verifikasi paginasi kembali ke halaman 1
39. Verifikasi node `All Groups` aktif
40. Buka halaman Fixed Asset > Settings > User di tab browser baru
41. Verifikasi Search di tab baru kosong
42. Verifikasi Filter di tab baru tidak aktif
43. Verifikasi Sort di tab baru default
44. Verifikasi node `All Groups` aktif di tab baru
45. Tutup tab baru dan kembali ke tab awal

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2, 4, dan 8 (pindah halaman pagination supaya isi halaman teramati, S-14); langkah 45 (menutup tab kedua, S-09). Langkah 1 TC-FA-SU-7 ("Klik node") dimulai dari langkah 6; pembukaan halaman dipenuhi hook `beforeEach` suite.
- Langkah 25 sampai 30 diamati sesudah Back lewat Breadcrumb; langkah 31 sampai 33 sesudah F5; langkah 34 sampai 39 sesudah klik ulang menu sidebar; langkah 40 sampai 44 pada tab baru.
- Urutan TC: TC-FA-SU-7 lebih dulu karena TC-FA-SU-8 membangun state (Search, Filter, Sort, node) yang dibersihkan klik ulang menu sidebar pada langkah 34 (S-10).
- Spec melewati sekitar 35 langkah (45 langkah). Seluruhnya satu kelas (screening filter dan retensi state User List, satu akun, tanpa mengubah data), dan tiap blok TC berdiri sendiri: kegagalan blok TC-FA-SU-7 tidak menghilangkan makna blok TC-FA-SU-8.
- Temuan untuk QA:
  - TC-FA-SU-8 langkah 1 menyebut "Filter Status `Active`" tanpa menyebut lokasi dan label tombol penerapan Filter; spec menulis "Terapkan Filter Status `Active`".
  - TC-FA-SU-8 langkah 5 membuka tab baru dan mengamati state awalnya; konteks kedua itu hanya dipakai untuk mengamati state awal (tanpa interaksi lintas tab), sehingga spec tetap di kelas fungsional. Bila pemilik proses menilai ini kelas multi-konteks, pindahkan langkah 40 sampai 45.
  - TC-FA-SU-7 Expected b menjelaskan pengguna yang muncul pada tiap node dengan keterangan dalam kurung (Group Role aktif pada node dan turunannya ditambah Total Control dan Read Only); spec hanya mengasersi daftar nama pengguna.
