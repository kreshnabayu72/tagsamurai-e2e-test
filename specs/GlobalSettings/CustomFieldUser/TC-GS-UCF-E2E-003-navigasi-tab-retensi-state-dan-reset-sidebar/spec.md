---
id: TC-GS-UCF-E2E-003-navigasi-tab-retensi-state-dan-reset-sidebar
title: "Navigasi Tab Custom Field: Breadcrumb Mengikuti Tab, F5, Back dan Forward, Retensi State Pindah Tab, dan Reset lewat Klik Ulang Sidebar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-3
  - TC-GS-UCF-4
  - TC-GS-UCF-398
  - TC-GS-UCF-399
  - TC-GS-UCF-400
coverage:
  web: automated
---

# Navigasi Tab Custom Field: Breadcrumb Mengikuti Tab, F5, Back dan Forward, Retensi State Pindah Tab, dan Reset lewat Klik Ulang Sidebar

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup, Client A). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > User pada sub-tab User List (Login User), sesuai precondition TC-GS-UCF-3, 399, dan 400. Navigasi antar-tab adalah objek uji sehingga langkah klik tab ditulis di `## Test Steps`.
- Data Pre-setup Client A (6 field, tetap di environment, hanya dibaca, tanpa suffix): `Cost Center`, `Employee Grade`, `Job Description`, `Bonus`, `Office Phone`, `Joining Date`.
- Population D-01 (8 field: `Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number`): di-seed lewat API di hook `before` (idempotent, dilewati bila sudah ada) sehingga tabel berisi tepat 14 field (precondition TC-GS-UCF-4 dan 398). Nama literal tanpa suffix karena asersi urutan A-Z dan hasil filter (pengecualian S-12 butir (i)); fixture baru `Fixture.customFieldUser.population`. Hook `after` hanya menghapus field Population yang dibuat hook `before` spec ini.
- Data Dinamis: tidak ada.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun Total Control dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: tombol Back dan Forward browser; muat ulang halaman (F5, tidak ada form terbuka sehingga tidak ada dialog `beforeunload`); pembacaan indikator filter aktif pada icon Filter.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`) dan state tabel (Search, Filter, Sort, ukuran halaman) yang dipulihkan langkah 44 dan 45 serta hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-3: Tab Custom Field dibuka dari tab bar halaman User dan Breadcrumb mengikuti tab aktif

1. Klik tab Custom Field
2. Verifikasi tab `Custom Field` aktif
3. Verifikasi tabel Custom Field termuat
4. Verifikasi Breadcrumb `User > Custom Field`
5. Klik tab Position
6. Verifikasi tab `Position` aktif dengan Breadcrumb `User > Position`
7. Verifikasi tabel Position tidak membawa Search, Filter, Sort, atau halaman milik Custom Field
8. Klik tab Custom Field
9. Verifikasi tab `Custom Field` kembali termuat dengan Breadcrumb `User > Custom Field`

### TC-GS-UCF-399: Muat ulang di tab Custom Field memuat tab Custom Field

10. Klik tab User List (kembali ke precondition: sub-tab Login User)
11. Klik tab Custom Field
12. Tekan F5
13. Verifikasi tab `Custom Field` aktif
14. Verifikasi Breadcrumb `User > Custom Field`
15. Verifikasi tab `User List` tidak menjadi tab aktif

### TC-GS-UCF-400: Tombol Back dan Forward browser berpindah antar-tab halaman User

16. Klik tab User List (kembali ke precondition: sub-tab Login User)
17. Klik tab Custom Field
18. Klik tab Position
19. Klik tombol Back browser
20. Verifikasi tab `Custom Field` aktif
21. Verifikasi Breadcrumb `User > Custom Field`
22. Klik tombol Forward browser
23. Verifikasi tab `Position` aktif
24. Verifikasi Breadcrumb `User > Position`

### TC-GS-UCF-4: Pindah tab Position lalu kembali ke Custom Field memulihkan Search, Filter, Sort, dan halaman tab Custom Field

25. Klik tab Custom Field
26. Ketik Search `phone`, tekan Enter
27. Klik Filter, pilih Data Type `Phone`, klik `[Apply]`
28. Klik header Field Name hingga sort descending aktif
29. Klik tab Position
30. Verifikasi tab Position tampil dengan state defaultnya sendiri
31. Verifikasi tab Position tidak membawa Search atau Filter tab Custom Field
32. Klik tab Custom Field
33. Verifikasi Search `phone` tetap terisi
34. Verifikasi filter Data Type `Phone` tetap aktif
35. Verifikasi sort Field Name descending tetap aktif
36. Verifikasi tabel menampilkan `Office Phone` lalu `Emergency Phone` (urutan Z-A)

### TC-GS-UCF-398: Klik ulang menu sidebar User mereset Filter, Sort, dan page size tab Custom Field

37. Klik menu sidebar Global Settings > User lalu klik tab Custom Field (mereset Search, Filter, dan Sort dari TC-GS-UCF-4 supaya tabel berada pada state default)
38. Klik Filter, pilih Data Type `Text`, klik `[Apply]`
39. Klik header Field Name hingga urutan Z-A (descending)
40. Ubah page size menjadi 25
41. Verifikasi tabel memuat sedikitnya satu baris
42. Verifikasi setiap baris tabel bertipe Text
43. Verifikasi urutan Field Name Z-A: `Tax ID`, `Employee Grade`, `badge number`
44. Klik menu sidebar Global Settings > User
45. Klik tab Custom Field
46. Verifikasi tidak ada filter ter-Apply
47. Verifikasi icon Filter tidak menampilkan indikator filter aktif
48. Verifikasi tabel menampilkan 10 baris halaman 1
49. Verifikasi urutan Field Name A-Z dengan `Annual Target` di baris pertama
50. Verifikasi page size kembali ke 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di spec: 3, 399, 400, 4, 398. TC yang berprecondition sub-tab User List (3, 399, 400) ditaruh lebih dulu; TC-GS-UCF-4 dan 398 yang mengubah Search, Filter, Sort, dan ukuran halaman ditaruh sesudahnya, dan TC-GS-UCF-398 terakhir karena langkah 5 TC itu mereset state yang dibangun TC-GS-UCF-4.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10 dan 16 (klik tab User List mengembalikan precondition "sub-tab Login User" TC-GS-UCF-399 dan 400), langkah 25 (membuka tab Custom Field sesuai precondition TC-GS-UCF-4 setelah TC sebelumnya berakhir di tab Position), dan langkah 37 (klik ulang sidebar lalu tab Custom Field untuk mereset state TC-GS-UCF-4; perilaku reset itu sendiri diasersi pada langkah 46 sampai 50).
- Langkah 41 (sedikitnya satu baris tampil) adalah baris pembanding sebelum asersi universal langkah 42 ("setiap baris bertipe Text"), bukan Expected TC (bagian 8b butir 2, S-03). Langkah 46 (tidak ada filter ter-Apply) beranchor langkah 47 dan 48 yang membuktikan tabel termuat.
- Pembagian TC lintas spec: retensi state Search, Filter, Sort, halaman, dan ukuran halaman lewat F5 (NC-28) ada di spec tabel utama (Search, Filter, Sort, Pagination); spec ini hanya memuat F5 untuk pemilihan tab (TC-GS-UCF-399).
- Spec melewati sekitar 35 langkah (50 langkah). Seluruhnya satu kelas (navigasi dan retensi state tab, satu akun, tanpa mengubah data), tiap blok TC berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-GS-UCF-3 Expected b ("tabel Position tidak membawa Search, Filter, Sort, atau halaman milik Custom Field") tidak punya state Custom Field yang dibangun sebelumnya di TC itu (langkah TC hanya klik tab), sehingga asersi tidak menguji pembawaan state; spec mengikuti TC dan pembawaan state diuji di TC-GS-UCF-4.
  - TC-GS-UCF-4 langkah 3 ("sampai descending") tidak menyebut jumlah klik; spec mengklik header Field Name hingga sort descending aktif.
  - TC-GS-UCF-4 Expected c ("state defaultnya sendiri") tidak menyebut isi state default tab Position; spec mengasersi tab Position tampil dengan state defaultnya dan tidak membawa Search atau Filter Custom Field.
  - TC-GS-UCF-400 Expected a menyebut tab Custom Field aktif setelah Back dan Position aktif setelah Forward; urutan riwayat dibentuk langkah 16 sampai 18 (klik tab User List, Custom Field, Position) dan tidak disebut eksplisit di TC.
