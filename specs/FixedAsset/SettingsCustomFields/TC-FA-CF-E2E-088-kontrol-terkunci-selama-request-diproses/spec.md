---
id: TC-FA-CF-E2E-088-kontrol-terkunci-selama-request-diproses
title: "Kontrol Terkunci Selama Request Create, Edit, dan Toggle Status Diproses"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-187
  - TC-FA-CF-315
  - TC-FA-CF-623
coverage:
  web: automated
---

# Kontrol Terkunci Selama Request Create, Edit, dan Toggle Status Diproses

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini membuat, mengubah, dan menonaktifkan field Company Alpha.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson, Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data baseline Company Alpha (Pre-setup #11 dan #12), tab General delapan baris: `Storage Capacity` (target Edit, langkah 11) dan `Asset Serial Tag` (target Toggle, langkah 21). Hook `before` memulihkan baseline lewat seed reset Company (disediakan tim FE/BE; fixture baru `Fixture.faCustomFields.baseline`); hook `after` memulihkan.
- Data Dinamis (dibuat spec lewat UI): `Saving {runId}-088` (Text, langkah 2) dan nama baru `Saving Edit {runId}-088` untuk `Storage Capacity` (langkah 12). Cleanup: hook `after` menghapus field bersuffix `{runId}-088` yang masih ada lewat API.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (Pre-setup #26): penyunting request/respons yang menunda respons Create, Edit, dan Deactivate selama 3 detik; penundaan hanya untuk mengamati state UI (bukan fault injection), dan intercept dilepas segera sesudah tiap blok (langkah 10, 20, dan 26).
- State global: tidak ada yang diubah selain data di atas dan flag Guided Tooltip (dipulihkan hook `after`).

## Test Steps

### TC-FA-CF-187: Selama Create diproses tombol dan kontrol form dikunci

1. Klik `[+ Custom Field]`
2. Isi Field Name `Saving {runId}-088`
3. Pilih Data Type `Text`
4. Tunda respons Create 3 detik
5. Klik `[Submit]`
6. Verifikasi tombol `[Submit]` menampilkan state loading
7. Verifikasi tombol `[Submit]` disabled
8. Verifikasi input, `[Clear Field]`, dan icon close `[✕]` disabled selama proses
9. Verifikasi modal Create tertutup setelah respons diterima
10. Lepas intercept respons Create

### TC-FA-CF-623: Selama Edit diproses tombol Save dan kontrol form dikunci

11. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
12. Ubah Field Name menjadi `Saving Edit {runId}-088`
13. Tunda respons Edit 3 detik
14. Klik `[Save]`
15. Verifikasi tombol `[Save]` menampilkan state loading
16. Verifikasi tombol `[Save]` disabled
17. Verifikasi input, `[Clear Field]`, dan icon close `[✕]` disabled selama proses
18. Verifikasi modal Edit tertutup setelah respons diterima
19. Verifikasi toast sukses `Success, custom field has been updated.` tampil
20. Lepas intercept respons Edit

### TC-FA-CF-315: Switch disabled selama request Deactivate diproses

21. Geser switch Active baris `Asset Serial Tag` ke OFF
22. Tunda respons Deactivate 3 detik
23. Klik `[Deactivate]` dan perhatikan switch
24. Verifikasi switch Active baris `Asset Serial Tag` disabled selama request berjalan
25. Verifikasi switch Active baris `Asset Serial Tag` aktif kembali setelah respons diterima
26. Lepas intercept respons Deactivate

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 187, 623, 315; urutan menyimpang dari urutan TC sumber (187, 315, 623) agar dua TC dengan modal (Create dan Edit) berurutan dan aksi Toggle di akhir. Spec ini tidak berisi aksi Delete.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10, 20, dan 26 (melepas intercept penahan respons segera setelah pemicu selesai; S-09). Tabel Alpha sembilan baris (delapan baseline ditambah `Saving {runId}-088`) berada di satu halaman sehingga Search tidak diperlukan.
- Penahanan respons (langkah 4, 13, dan 22) hanya untuk mengamati state loading dan disabled; tidak termasuk fault injection kelas b (bagian 3 prinsip 13b).
- Asersi tambahan di luar Expected TC (S-03): langkah 6 dan 7, 15 dan 16 memecah "loading dan disabled" menjadi dua `Verifikasi` (spinner dan state tombol adalah klausa terpisah).
- Temuan untuk QA:
  - TC-FA-CF-187 butir c menulis "Setelah respons kontrol aktif kembali atau modal tertutup" (kondisi "atau"); spec mengasersi hasil yang konsisten dengan Create sukses, yaitu modal Create tertutup (langkah 9). TC-FA-CF-623 butir c sudah menyebut modal tertutup.
  - TC-FA-CF-187 tidak menyebut apakah toast sukses Create tampil sesudah respons; tidak diasersi.
  - TC-FA-CF-315 tidak menyebut kapan dialog konfirmasi Deactivate tertutup relatif terhadap pengamatan switch; spec mengikuti urutan langkah TC.
