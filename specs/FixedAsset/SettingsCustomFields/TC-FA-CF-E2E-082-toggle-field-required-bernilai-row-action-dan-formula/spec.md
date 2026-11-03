---
id: TC-FA-CF-E2E-082-toggle-field-required-bernilai-row-action-dan-formula
title: "Toggle Status: Field Required, Pemulihan Nilai, Menu Row Action, dan Field Formula"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-312
  - TC-FA-CF-313
  - TC-FA-CF-314
  - TC-FA-CF-316
coverage:
  web: automated
---

# Toggle Status: Field Required, Pemulihan Nilai, Menu Row Action, dan Field Formula

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini menonaktifkan dan mengaktifkan field baseline serta membaca form registrasi aset dan Detail aset.
- Akun aktor: Total Control Company Nilai (Pre-setup #18; pengguna Sarah Johnson, Modified By `Sarah J`), kredensial `Spectra.env.FA_TC_NILAI_PASSWORD`. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Company Nilai (Pre-setup #18, memuat baseline Company Alpha #11 dan #12 serta field dan aset tambahan; Max custom fields per asset name 20): `Asset Serial Tag` (Text, Required Yes, Active), `Total Cost` (Formula, Active), `Maintenance Note` (Text General, Active, bernilai `Checked` pada aset `A1`), aset `A1` (Asset Name `Pump`, Active). Hook `before` memulihkan baseline lewat seed reset Company (disediakan tim FE/BE; fixture baru `Fixture.faCustomFields.nilai`); spec ini menonaktifkan `Total Cost` dan `Asset Serial Tag` sehingga Last Updated keduanya berubah sampai seed reset berikutnya, dipulihkan hook `after`. Tabel Company Nilai memuat lebih dari sepuluh baris sehingga ukuran halaman diatur 25 (Pagination 10, 25, 50, dan 100).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: membuka form registrasi aset (modul Asset Registration) dan form edit aset lama serta menyimpannya; membuka Detail aset (Pre-setup #31). Teks UI lintas modul diasersi hanya sejauh teks Expected TC.
- State global: tidak ada yang diubah selain status field baseline dan flag Guided Tooltip (dipulihkan hook `after`).

## Test Steps

1. Pilih ukuran halaman 25 pada Pagination

### TC-FA-CF-314: Menu row action tidak memuat Activate maupun Deactivate

2. Klik row action `⋯` baris `Asset Serial Tag`
3. Verifikasi menu hanya memuat `Edit` (icon Edit2Line) dan `Delete` (icon DeleteBin6Line, danger)
4. Verifikasi menu tidak memuat `Activate` maupun `Deactivate`
5. Tekan `Esc`

### TC-FA-CF-316: Deactivate field bertipe Formula

6. Geser switch Active baris `Total Cost` ke OFF
7. Verifikasi dialog `Deactivate Custom Field` dengan bullet `• Total Cost` tampil
8. Klik `[Deactivate]`
9. Verifikasi switch Active baris `Total Cost` berada di posisi OFF
10. Verifikasi toast sukses `Success, custom field has been deactivated.` tampil

### TC-FA-CF-312: Deactivate field Required tidak memblokir aset lama

11. Geser switch Active baris `Asset Serial Tag` ke OFF
12. Klik `[Deactivate]`
13. Tunggu aksi selesai (switch baris `Asset Serial Tag` berada di posisi OFF)
14. Buka form registrasi aset untuk Asset Name `Pump`
15. Verifikasi field `Asset Serial Tag` tidak tampil dan tidak diwajibkan pada form registrasi aset
16. Buka form edit aset lama `A1`
17. Simpan form edit aset `A1` tanpa mengubah apa pun
18. Verifikasi aset `A1` tersimpan tanpa error validasi sehingga tetap valid

### TC-FA-CF-313: Deactivate lalu Activate memulihkan field dan nilai

19. Buka Fixed Asset > Settings > Custom Fields (tab General)
20. Pilih ukuran halaman 25 pada Pagination
21. Geser switch Active baris `Maintenance Note` ke OFF
22. Klik `[Deactivate]`
23. Geser switch Active baris `Maintenance Note` ke ON
24. Klik `[Activate]`
25. Tunggu aksi selesai (switch baris `Maintenance Note` berada di posisi ON)
26. Buka Detail aset `A1`
27. Verifikasi Detail aset `A1` menampilkan kembali field `Maintenance Note` dengan nilai `Checked` (data nilai tidak pernah dihapus)

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 314 (tanpa mutasi), 316, 312, 313 (form registrasi aset dan Detail aset dibuka paling akhir sehingga navigasi keluar dari layar Custom Fields hanya dua kali). Urutan menyimpang dari urutan TC sumber (312, 313, 314, 316).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 20 (ukuran halaman 25 agar baris target Company Nilai tampil tanpa Search), langkah 5 (menutup menu row action), langkah 13 dan 25 (menunggu aksi tanpa asersi selesai sebelum berpindah surface), dan langkah 19 (kembali ke layar Custom Fields).
- TC-FA-CF-312, 314, dan 316 menyebut Company Alpha dengan baseline Pre-setup #11 dan #12, sedangkan TC-FA-CF-313 menyebut Company Nilai. Spec menjalankan keempat TC di Company Nilai karena Company itu memuat baseline Company Alpha yang sama (Pre-setup #18) sehingga tidak ada pergantian akun atau Company di tengah spec.
- Asersi tambahan di luar Expected TC (S-03): langkah 4 memecah "Menu hanya memuat Edit dan Delete" TC-FA-CF-314 menjadi daftar isi menu (langkah 3) dan ketiadaan `Activate` serta `Deactivate` (langkah 4); langkah 14 memakai nama `Pump` sebagai Asset Name pada "Asset Name apa pun" TC-FA-CF-312.
- Temuan untuk QA:
  - TC-FA-CF-316 berjudul "Deactivate dan Activate", tetapi Langkah Uji dan Expected hanya Deactivate; Activate field Formula tidak diuji (spec 081 menguji dialog Activate field non-Formula).
  - TC-FA-CF-314 Expected "status diubah hanya lewat switch dan Bulk Action Bar" adalah kesimpulan desain yang tidak teramati terpisah di UI; tidak diasersi sendiri.
  - TC-FA-CF-313 Expected "data nilai tidak pernah dihapus" adalah kesimpulan dari nilai `Checked` yang tampil kembali; ditulis satu `Verifikasi` (langkah 27).
  - Tata letak dan label form registrasi aset, form edit aset, dan Detail aset tidak didefinisikan PRD modul ini (NC-01); langkah 14 sampai 18 dan 26 memakai istilah TC. TC-FA-CF-312 tidak menyebut kontrol penyimpanan form edit aset.
  - TC-FA-CF-312 Expected "tidak diwajibkan" untuk field yang tidak tampil adalah kesimpulan dari field tersembunyi; ditulis satu `Verifikasi` bersama "tidak tampil" (langkah 15; S-03).
  - Email akun Total Control Company Nilai tidak ada di Pre-setup TC.
