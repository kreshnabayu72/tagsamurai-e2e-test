---
id: TC-FA-CF-E2E-087-klik-ganda-cepat-pada-konfirmasi-delete-dan-bulk-delete
title: "Klik Ganda Cepat pada Konfirmasi Delete dan Bulk Delete"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-628
  - TC-FA-CF-636
coverage:
  web: automated
---

# Klik Ganda Cepat pada Konfirmasi Delete dan Bulk Delete

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini menghapus field milik sendiri di Company Alpha dan membaca Changelog permanen yang dibagi suite.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson, Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data baseline Company Alpha (Pre-setup #11 dan #12): delapan field tab General tidak diubah spec ini. Hook `before` memulihkan baseline lewat seed reset Company (disediakan tim FE/BE; fixture baru `Fixture.faCustomFields.baseline`).
- Data Dinamis (di-seed lewat API di hook `before`, bersuffix per run): `Del Dbl {runId}-087` (Text, Active; target TC-FA-CF-628), `Bulk Del A {runId}-087` dan `Bulk Del B {runId}-087` (Text, Active; target TC-FA-CF-636). Dengan tiga field ini tabel memuat sebelas baris sehingga baris target ditemukan lewat Search. Cleanup: hook `after` menghapus field bersuffix `{runId}-087` yang masih ada lewat API tanpa mengandalkan seeding berhasil penuh.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: klik ganda cepat pada tombol `[Delete]` dialog; Search tabel Custom Fields dan Modal Changelog; menunggu toast sukses lama hilang otomatis; interception respons yang menunda respons Delete dan Bulk Delete selama 3 detik (Pre-setup #26), hanya untuk mengamati state UI (bukan fault injection) dan dilepas segera sesudah asersi state sementara (langkah 7 dan 21).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook `after`).

## Test Steps

### TC-FA-CF-628: Klik ganda cepat pada konfirmasi Delete

1. Ketik Search `Del Dbl {runId}-087`, tekan Enter
2. Klik row action `⋯` > `Delete` pada baris `Del Dbl {runId}-087`
3. Tunda respons Delete 3 detik
4. Klik `[Delete]` dua kali dengan cepat
5. Verifikasi tombol `[Delete]` menampilkan state loading setelah klik pertama
6. Verifikasi tombol `[Delete]` disabled setelah klik pertama
7. Lepas tahanan respons Delete
8. Verifikasi toast `Success, custom field has been deleted.` tampil sekali
9. Klik icon Changelog
10. Ketik Search `Del Dbl {runId}-087` pada Modal Changelog, tekan Enter
11. Verifikasi Modal Changelog memuat tepat satu baris Action `Delete` untuk `Del Dbl {runId}-087`
12. Tutup modal Changelog dengan `✕`

### TC-FA-CF-636: Klik ganda cepat pada konfirmasi Bulk Delete

13. Tunggu toast dari langkah 8 hilang otomatis
14. Ganti isi kotak search dengan `Bulk Del`, tekan Enter
15. Centang baris `Bulk Del A {runId}-087` dan `Bulk Del B {runId}-087`
16. Klik `[Delete]` pada Bulk Action Bar
17. Tunda respons Bulk Delete 3 detik
18. Klik `[Delete]` pada dialog dua kali dengan cepat
19. Verifikasi tombol konfirmasi dialog menampilkan state loading setelah klik pertama
20. Verifikasi tombol konfirmasi dialog disabled setelah klik pertama
21. Lepas tahanan respons Bulk Delete
22. Verifikasi toast `Success, custom field has been deleted.` tampil sekali
23. Klik icon Changelog
24. Ketik Search `Bulk Del` pada Modal Changelog, tekan Enter
25. Verifikasi Modal Changelog memuat tepat satu baris Action `Bulk Delete` per field, yaitu `Bulk Del A {runId}-087` dan `Bulk Del B {runId}-087` (dua baris Bulk Delete total)
26. Tutup modal Changelog dengan `✕`

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 628 lalu 636 (keduanya aksi Delete, paling akhir; S-10); sama dengan urutan TC sumber.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3 dan 17 (menunda respons 3 detik sebelum klik ganda; Pre-setup #26), langkah 7 dan 21 (melepas tahanan respons sesudah asersi state sementara; asersi toast `tampil sekali` ditulis sesudahnya karena selama respons ditahan toast hasil belum muncul, bagian 8b butir 11), langkah 1 dan 14 (Search agar baris target tampil), langkah 9 dan 23 (membuka Modal Changelog), langkah 10 dan 24 (Search entri), langkah 12 dan 26 (menutup modal Changelog), dan langkah 13 (menunggu toast sukses lama hilang otomatis supaya hitungan toast pada langkah 22 hanya memuat toast hasil klik ganda langkah 18).
- Asersi tambahan di luar Expected TC (S-03): langkah 5 dan 6 serta 19 dan 20 memecah "state loading dan disabled" menjadi dua `Verifikasi` (spinner dan state tombol adalah klausa terpisah) dan mendahului asersi hasil (bagian 8b butir 5) dan ditulis selagi respons masih ditahan.
- Data milik spec (S-06, S-12): TC-FA-CF-628 dan TC-FA-CF-636 menyebut field Pre-setup `Legacy Tag` dan `Compliance File`; spec memakai field Dinamis bersuffix `{runId}-087` agar jumlah baris Delete pada Changelog permanen dapat diasersi dari baseline nol (S-12), tanpa menghapus field Pre-setup bersama.
- Temuan untuk QA:
  - TC-FA-CF-628 butir c mengasersi satu baris Action `Delete` pada Changelog tanpa menyebut baseline; spec memakai nama field bersuffix unik sebagai baseline nol.
