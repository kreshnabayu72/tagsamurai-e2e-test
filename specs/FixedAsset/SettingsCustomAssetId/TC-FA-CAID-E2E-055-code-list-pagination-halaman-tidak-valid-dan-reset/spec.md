---
id: TC-FA-CAID-E2E-055-code-list-pagination-halaman-tidak-valid-dan-reset
title: "Modal View Code List: Halaman Tidak Valid, Ganti Page Size, Sort, dan Search Mereset Halaman"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-144
  - TC-FA-CAID-145
  - TC-FA-CAID-146
  - TC-FA-CAID-147
coverage:
  web: automated
---

# Modal View Code List: Halaman Tidak Valid, Ganti Page Size, Sort, dan Search Mereset Halaman

## Prerequisites

- Mode: FE+BE (isi Code List dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun aktor: Total Control `Company Volume` (Pre-setup No 16, akun sendiri, bukan akun Pre-setup No 1); email disediakan tim FE/BE (Pre-setup No 16), kredensial `Spectra.env.FA_VOLUME_TC_PASSWORD` (nama usulan, didaftarkan di tahap script). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`).
- Environment variable: `FA_VOLUME_TC_PASSWORD` (Total Control Company Volume) dan `FA_TC_PASSWORD` (akun default suite). Password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen` untuk akun Company Volume; baseline konfigurasi dan aset Company Alpha (Pre-setup No 10 dan 11) tidak dipakai spec ini; layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Data Pre-setup No 16 (`Company Volume`): 120 Group ber-Code `Volume Group 001` sampai `Volume Group 120` (Code `VG001` sampai `VG120`). Company khusus yang terpisah dari Company Alpha; dataset disediakan tim FE/BE pada Company itu (dikembalikan ke keadaan awal sebelum tiap run). Spec hanya membaca.
- Data Dinamis: tidak ada. State global: tidak ada yang diubah.

## Test Steps

### TC-FA-CAID-144: Nomor halaman tidak valid diabaikan

1. Klik tautan `[View Code List]`
2. Ketik `0` pada input nomor halaman, tekan Enter
3. Verifikasi tabel tetap di halaman 1 untuk input `0`
4. Verifikasi tidak ada pesan error untuk input `0`
5. Ganti isi input nomor halaman dengan `99`, tekan Enter
6. Verifikasi tabel tetap di halaman 1 untuk input `99`
7. Verifikasi tidak ada pesan error untuk input `99`
8. Ganti isi input nomor halaman dengan `abc`, tekan Enter
9. Verifikasi tabel tetap di halaman 1 untuk input `abc`
10. Verifikasi tidak ada pesan error untuk input `abc`

### TC-FA-CAID-146: Mengganti sort tetap di nomor halaman sekarang

11. Pindah ke halaman 2
12. Klik header `Code` dua kali
13. Verifikasi halaman 2 tetap aktif
14. Verifikasi halaman 2 menampilkan `Volume Group 110` sampai `Volume Group 101` (Code `VG110` sampai `VG101`) berurutan Descending
15. Klik header `Code` sekali lagi (sort kembali default)

### TC-FA-CAID-147: Search di halaman lebih dari 1 mereset ke halaman 1

16. Pindah ke halaman 3
17. Ketik Search `Volume Group 05`, tekan Enter
18. Verifikasi halaman 1 aktif
19. Verifikasi hasil `Volume Group 050` sampai `Volume Group 059`
20. Klik `(←)` pada kotak Search

### TC-FA-CAID-145: Mengganti page size kembali ke halaman 1

21. Pindah ke halaman 2
22. Pilih page size `25`
23. Verifikasi halaman 1 aktif
24. Verifikasi 25 baris `Volume Group 001` sampai `Volume Group 025`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 24 langkah.
- Urutan TC di dalam spec: TC-FA-CAID-144, 146, 147, lalu 145. TC-FA-CAID-145 mengubah page size menjadi 25 sehingga ditaruh paling akhir; TC-FA-CAID-146 dan 147 membutuhkan 10 baris per halaman.
- Langkah penghubung (tanpa `Verifikasi`): langkah 15 (klik ketiga mengembalikan sort ke default sebelum TC-FA-CAID-147) dan langkah 20 (klik `(←)` mengosongkan Search sebelum TC-FA-CAID-145, S-09).
- Asersi absence "tidak ada pesan error" didahului `Verifikasi` tabel tetap di halaman 1 pada input yang sama (tabel termuat dan terbaca).
- Pembagian TC lintas spec: TC-FA-CAID-120, 142, dan 143 ada di spec 054.
- Alasan topik Modal View Code List berada di beberapa spec (bagian 3 prinsip 1): tiap spec memakai dataset berbeda. Spec ini memakai `Company Volume` (Pre-setup No 16, kelas e) dengan akun sendiri, dataset yang sama dengan spec 054; dataset tetap Pre-setup No 28 ada di spec 049 dan `Company Code List Khusus` (Pre-setup No 34) di spec 050. Ukuran gabungan spec ini dan spec 054 (24 dan 48 langkah) melebihi sekitar 35 langkah.
- Temuan untuk QA:
  - Pre-setup No 16 mensyaratkan Company khusus dengan akun sendiri; email akun dan nama env var password tidak tertulis (email "disediakan tim FE/BE"), sehingga spec memakai usulan `FA_VOLUME_TC_PASSWORD`.
