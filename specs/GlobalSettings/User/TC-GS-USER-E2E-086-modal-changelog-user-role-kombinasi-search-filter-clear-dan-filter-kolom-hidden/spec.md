---
id: TC-GS-USER-E2E-086-modal-changelog-user-role-kombinasi-search-filter-clear-dan-filter-kolom-hidden
title: "Modal Changelog Role: kombinasi Search dan Filter, Clear, filter kolom hidden, nol baris"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-527
  - TC-GS-USER-528
  - TC-GS-USER-529
  - TC-GS-USER-530
  - TC-GS-USER-531
coverage:
  web: automated
---

# Modal Changelog Role: kombinasi Search dan Filter, Clear, filter kolom hidden, nol baris

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control Siti Nurhaliza (`Siti N`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 2), akun default suite. Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User).
- Pelaku seeding lewat sesi API (tidak login UI): Manage user and role (Full CRUD) Fajar Nugroho (`Fajar N`), `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 4), `Spectra.env.GS_FULLCRUD_PASSWORD`. Fajar menjadi nilai Modified By kedua selain `Siti N`.
- Environment variable: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: tidak dipakai. TC menyebut `Ahmad Fauzi` (Tabel Data Uji Pre-setup baris 13); aksi tulis Role memakai user seed milik spec (S-06), jadi Pre-setup tidak diubah.
- Data Dinamis: user seed `Ahmad Fauzi {runId}-086`, email `ahmadfauzi+{runId}-086@qwertysystem.net`, Access `Global Settings`, bukan tier, field wajib lain diisi seadanya oleh seeding.
- Seeding minimal (S-11; lewat API di hook `before`, urutan sebagai berikut; setara TC-GS-USER-902, 903, 904, 1052). Entri yang diasersi:
  - 1. Siti N: Assign `Manage TAG` -> `Assign | Manage TAG | Access | — | Assigned | Siti N`.
  - 2. Siti N: centang Update `Manage TAG` -> `Edit | Manage TAG | Update | Inactive | Active | Siti N`.
  - 3. Fajar N: Assign `Manage files` -> `Assign | Manage files | Access | — | Assigned | Fajar N`.
  - 4. Siti N: Remove `Manage files` -> `Remove | Manage files | Access | Assigned | — | Siti N`.
  - 5. Siti N: centang Read `Manage hardware` -> `Assign | Manage hardware | Access | — | Assigned | Siti N`.
  - 6. Fajar N: centang Update `Manage hardware` -> `Edit | Manage hardware | Update | Inactive | Active | Fajar N`.
  - Nilai distinct (S-11): Action 3 (`Assign`, `Edit`, `Remove`), Role 3, Field 2 (`Access`, `Update`), Modified By 2 (`Siti N`, `Fajar N`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus user seed lewat API; pulihkan visibilitas kolom Modal Changelog Role ke default (7 kolom tampil) lewat penghapusan key `localStorage` tabel itu (nama key disediakan tim FE). Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: mengetik kotak Search modal; membaca state icon Filter (aktif gelap) dan arah sort; membaca dan menghapus key `localStorage`.
- Precondition TC-GS-USER-527 sampai 531: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); data pre-setup User tersedia; riwayat Changelog Role user seed terisi.
- Suite serial (`parallel: false`), lihat `suite.md`.
- State global yang dipulihkan: visibilitas kolom Modal Changelog Role (default).

## Test Steps

### TC-GS-USER-527: Search lalu Filter menghasilkan irisan

1. Klik Name `Ahmad Fauzi {runId}-086` di User List
2. Klik Tab `Role`
3. Klik icon Changelog di toolbar Tab Role
4. Klik icon Search, ketik `assign`, tekan Enter
5. Verifikasi baris Action `Assign` Role `Manage TAG` Modified By `Siti N` tampil (pembanding hasil Search saja)
6. Klik icon Filter, pilih opsi Modified By `Fajar N`, klik `[Apply]`
7. Verifikasi hasil = Search ∩ Filter (baris Action `Assign` Role `Manage files` Modified By `Fajar N` tampil)
8. Verifikasi baris Action `Assign` Role `Manage TAG` Modified By `Siti N` tidak tampil
9. Verifikasi baris Action `Edit` Role `Manage hardware` Modified By `Fajar N` tidak tampil
10. Verifikasi keyword tidak ter-reset (isi Search tetap `assign`)
11. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
12. Klik icon `(×)`, lalu tekan Enter pada input kosong

### TC-GS-USER-528: Filter lalu Search menghasilkan irisan

13. Klik icon Filter, pilih opsi Action `Edit`, klik `[Apply]`
14. Verifikasi baris Action `Edit` Role `Manage TAG` tampil (pembanding hasil Filter saja)
15. Isi Search dengan `hardw`, tekan Enter
16. Verifikasi hasil = Filter ∩ Search (baris Action `Edit` Role `Manage hardware` tampil)
17. Verifikasi baris Action `Edit` Role `Manage TAG` tidak tampil
18. Verifikasi Filter tetap aktif (baris Action `Assign` Role `Manage hardware` tidak tampil)
19. Verifikasi icon Filter berubah gelap
20. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
21. Klik icon `(×)`, lalu tekan Enter pada input kosong

### TC-GS-USER-531: Kombinasi Search dan Filter menghasilkan 0 baris lalu pulih

22. Isi Search dengan `remov`, tekan Enter
23. Verifikasi baris Action `Remove` Role `Manage files` tampil
24. Klik icon Filter, pilih opsi Action `Assign` (tidak beririsan dengan hasil Search), klik `[Apply]`
25. Verifikasi empty filtered state: teks `No results found`
26. Verifikasi empty filtered state: teks `Try adjusting your search or filter.`
27. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
28. Verifikasi baris Action `Remove` Role `Manage files` tampil kembali
29. Klik icon `(×)`, lalu tekan Enter pada input kosong

### TC-GS-USER-529: Clear filter saat Search dan Sort aktif

30. Isi Search dengan `assign`, tekan Enter
31. Klik header Action
32. Verifikasi sort Action ascending A-Z aktif (pembanding sebelum Clear)
33. Klik icon Filter, pilih opsi Modified By `Siti N`, klik `[Apply]`
34. Verifikasi baris Action `Assign` Role `Manage TAG` Modified By `Siti N` tampil
35. Verifikasi baris Action `Assign` Role `Manage files` Modified By `Fajar N` tidak tampil
36. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
37. Verifikasi keyword tetap aktif (isi Search tetap `assign`)
38. Verifikasi arah sort Action tetap ascending A-Z
39. Verifikasi filter terlepas (baris Action `Assign` Role `Manage files` Modified By `Fajar N` tampil kembali)
40. Klik header Action dua kali (Action descending, lalu kembali ke default sort tabel)
41. Klik icon `(×)`, lalu tekan Enter pada input kosong

### TC-GS-USER-530: Filter tetap tersedia untuk kolom yang di-hide

42. Klik icon Filter, pilih opsi Modified By `Fajar N`, klik `[Apply]`
43. Verifikasi baris Action `Assign` Role `Manage files` tampil (pembanding sebelum kolom di-hide)
44. Verifikasi baris Action `Assign` Role `Manage TAG` tidak tampil
45. Klik header kolom Column Visibility (⋯), hilangkan centang `Modified By` pada overlay, lalu tutup overlay
46. Verifikasi Filter tetap aktif menyaring (baris Action `Assign` Role `Manage files` tampil)
47. Verifikasi Filter tetap aktif menyaring (baris Action `Assign` Role `Manage TAG` tidak tampil)
48. Klik icon Filter
49. Verifikasi field filter `Modified By` tetap ada di Filter Panel
50. Klik `[Clear Field]`, lalu klik `[Apply]`
51. Klik header kolom Column Visibility (⋯), centang kembali `Modified By` pada overlay, lalu tutup overlay

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Modal Changelog Role dibuka sekali di langkah 1 sampai 3 untuk semua TC.
- Urutan TC dalam spec: TC-GS-USER-527, 528, 531, 529, 530. Alasan: TC-GS-USER-531 (empty state, lalu pulih) memakai Search dan Filter tanpa Sort sehingga ditaruh sebelum TC-GS-USER-529 yang mengubah sort; TC-GS-USER-530 di akhir karena mengubah visibilitas kolom (preferensi di `localStorage`) dan memulihkannya di langkah 51.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11, 20, 27, 36, dan 50 (`[Clear Field]` + `[Apply]` untuk melepas filter), langkah 12, 21, 29, dan 41 (mengosongkan Search dan mereset tabel), langkah 40 (mengembalikan sort Action ke default), dan langkah 45 dan 51 (membuka dan menutup overlay Column Visibility; hide dan unhide adalah aksi TC).
- Langkah 5, 14, 23, 32, 34, 43 adalah anchor positif untuk asersi ketiadaan baris (S-03, bagian 8b butir 2). Pada TC-GS-USER-527 dan 528, pasangan nilai baris dipilih sehingga satu baris cocok dengan Search tetapi tidak dengan Filter, dan satu baris sebaliknya; ketiadaannya membuktikan tiap kontrol tetap berlaku.
- Pada TC-GS-USER-530 kolom yang difilter dan di-hide adalah Modified By; baris diidentifikasi lewat kolom Action dan Role yang tetap tampil.
- Spec melewati sekitar 35 langkah (51 langkah) karena tiap Expected bermajemuk TC-GS-USER-527, 528, 529, dan 531 menjadi satu `Verifikasi` per klausa (S-01) dan tiap TC perlu pembersihan filter dan Search di akhir. Semua blok satu kelas harness (kombinasi Search dan Filter satu Modal Changelog Role), satu akun, satu dataset, dan tiap blok berdiri sendiri karena Search dan Filter dilepas di akhir blok; modal dibuka sekali.
- TC terbagi lintas spec: screening dan opsi Filter Panel ada di spec 085; Sort dan Pagination serta kombinasi empat kontrol (TC-GS-USER-550) ada di spec 087.
- Temuan untuk QA: (1) TC-GS-USER-527, 528, 529, 531 menyebut "keyword", "terapkan filter", dan "filter yang tidak beririsan" tanpa nilai; spec menetapkan nilai konkret dari data seeding. (2) TC-GS-USER-529 dan 530 "salah satu kolom" tidak menyebut kolom; spec memakai Action (sort) dan Modified By (filter). (3) TC-GS-USER-531 Expected a tidak menyebut teks empty filtered state; spec memakai teks yang sama dengan TC-GS-USER-517. (4) TC-GS-USER-527 sampai 531 menyebut `Ahmad Fauzi` tanpa suffix; spec memakai user seed bersuffix.
