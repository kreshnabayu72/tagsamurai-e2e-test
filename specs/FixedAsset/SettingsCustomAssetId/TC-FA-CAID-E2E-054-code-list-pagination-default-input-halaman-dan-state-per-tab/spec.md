---
id: TC-FA-CAID-E2E-054-code-list-pagination-default-input-halaman-dan-state-per-tab
title: "Modal View Code List: Pagination 120 Baris per Tab, State per Tab, dan Input Halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-120
  - TC-FA-CAID-142
  - TC-FA-CAID-143
coverage:
  web: automated
---

# Modal View Code List: Pagination 120 Baris per Tab, State per Tab, dan Input Halaman

## Prerequisites

- Mode: FE+BE (isi Code List dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun aktor: Total Control `Company Volume` (Pre-setup No 16, akun sendiri, bukan akun Pre-setup No 1); email disediakan tim FE/BE (Pre-setup No 16), kredensial `Spectra.env.FA_VOLUME_TC_PASSWORD` (nama usulan, didaftarkan di tahap script). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`).
- Environment variable: `FA_VOLUME_TC_PASSWORD` (Total Control Company Volume) dan `FA_TC_PASSWORD` (akun default suite). Password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen` untuk akun Company Volume; baseline konfigurasi dan aset Company Alpha (Pre-setup No 10 dan 11) tidak dipakai spec ini; layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Data Pre-setup No 16 (`Company Volume`): 120 master ber-Code pada tiap tab: Group `Volume Group 001` sampai `Volume Group 120` (Code `VG001` sampai `VG120`), Category `Volume Category 001` sampai `120` (Code `VC001` sampai `VC120`), Asset Name `Volume Asset 001` sampai `120` (Code `VA001` sampai `VA120`), Division `Volume Division 001` sampai `120` (Code `VD001` sampai `VD120`), Account Active `Volume Account 001` sampai `120` (Code `2001` sampai `2120`). Company khusus yang terpisah dari Company Alpha; dataset disediakan tim FE/BE pada Company itu (dikembalikan ke keadaan awal sebelum tiap run). Spec hanya membaca.
- Data Dinamis: tidak ada. State global: tidak ada yang diubah. Total tiap tab (120) berasal dari seeding.

## Test Steps

### TC-FA-CAID-142: Pagination pada lima tab

1. Klik tautan `[View Code List]`
2. Verifikasi `Group Codes`: halaman 1 menampilkan 10 baris `Volume Group 001` sampai `Volume Group 010`
3. Buka pilihan page size
4. Verifikasi pilihan page size `10`, `25`, `50`, `100` tanpa opsi `All`
5. Pilih page size `10` (menutup pilihan tanpa mengubah ukuran)
6. Klik tab `Category Codes`
7. Verifikasi `Category Codes`: halaman 1 menampilkan 10 baris `Volume Category 001` sampai `Volume Category 010`
8. Buka pilihan page size
9. Verifikasi pilihan page size `10`, `25`, `50`, `100` tanpa opsi `All`
10. Pilih page size `10` (menutup pilihan tanpa mengubah ukuran)
11. Klik tab `Asset Name Codes`
12. Verifikasi `Asset Name Codes`: halaman 1 menampilkan 10 baris `Volume Asset 001` sampai `Volume Asset 010`
13. Buka pilihan page size
14. Verifikasi pilihan page size `10`, `25`, `50`, `100` tanpa opsi `All`
15. Pilih page size `10` (menutup pilihan tanpa mengubah ukuran)
16. Klik tab `Division Codes`
17. Verifikasi `Division Codes`: halaman 1 menampilkan 10 baris `Volume Division 001` sampai `Volume Division 010`
18. Buka pilihan page size
19. Verifikasi pilihan page size `10`, `25`, `50`, `100` tanpa opsi `All`
20. Pilih page size `10` (menutup pilihan tanpa mengubah ukuran)
21. Klik tab `Account Codes`
22. Verifikasi `Account Codes`: halaman 1 menampilkan 10 baris `Volume Account 001` sampai `Volume Account 010`
23. Buka pilihan page size
24. Verifikasi pilihan page size `10`, `25`, `50`, `100` tanpa opsi `All`
25. Pilih page size `10` (menutup pilihan tanpa mengubah ukuran)

### TC-FA-CAID-143: Input nomor halaman langsung

26. Klik tab `Group Codes`
27. Ketik `3` pada input nomor halaman, tekan Enter
28. Verifikasi halaman 3 aktif menampilkan `Volume Group 021` sampai `Volume Group 030`

### TC-FA-CAID-120: State Search, Sort, dan paginasi per tab

29. Ketik Search `Volume Group 1`, tekan Enter
30. Klik header `Code` dua kali (Descending)
31. Pindah ke halaman 2
32. Klik tab `Category Codes`
33. Verifikasi tab `Category Codes`: Search kosong
34. Verifikasi tab `Category Codes`: sort Name A-Z
35. Verifikasi tab `Category Codes`: halaman 1
36. Klik tab `Group Codes`
37. Verifikasi tab `Group Codes` masih berisi keyword `Volume Group 1`
38. Verifikasi tab `Group Codes`: `Code` Descending
39. Verifikasi tab `Group Codes`: halaman 2 menampilkan `Volume Group 110` sampai `Volume Group 101`
40. Klik `[✕]` pada header modal
41. Klik tautan `[View Code List]`
42. Verifikasi tab `Group Codes` kembali ke state default: Search kosong
43. Verifikasi tab `Group Codes` kembali ke state default: sort Name A-Z
44. Verifikasi tab `Group Codes` kembali ke state default: halaman 1
45. Klik tab `Category Codes`
46. Verifikasi tab `Category Codes` kembali ke state default: Search kosong
47. Verifikasi tab `Category Codes` kembali ke state default: sort Name A-Z
48. Verifikasi tab `Category Codes` kembali ke state default: halaman 1

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 48 langkah, di atas 35 langkah. Alasan: ketiga TC memakai dataset yang sama (Pre-setup No 16, volume 120 baris per tab, kelas e) dan berdiri sendiri (TC-FA-CAID-142 hanya membaca tiap tab, TC-FA-CAID-143 membuka satu halaman, TC-FA-CAID-120 menutup dan membuka kembali modal); langkah per tab pada TC-FA-CAID-142 (klik tab, `Verifikasi` baris, buka pilihan page size, `Verifikasi` opsi, pilih `10`) adalah ekspansi lima tab dengan parameter yang tertulis di langkah.
- Urutan TC di dalam spec: TC-FA-CAID-142, 143, lalu 120. TC-FA-CAID-120 mengubah Search, Sort, dan halaman lalu menutup modal, sehingga ditaruh paling akhir.
- Langkah penghubung (tanpa `Verifikasi`): pilih page size `10` pada tiap tab TC-FA-CAID-142 (menutup pilihan tanpa mengubah ukuran halaman) dan langkah 26 (kembali ke tab `Group Codes`).
- Pembagian TC lintas spec: TC-FA-CAID-144 sampai 147 ada di spec 055.
- Alasan topik Modal View Code List berada di beberapa spec (bagian 3 prinsip 1): tiap spec memakai dataset berbeda. Spec ini memakai `Company Volume` 120 master per tab (Pre-setup No 16, kelas e) dengan akun sendiri; dataset tetap Pre-setup No 28 ada di spec 049 dan `Company Code List Khusus` (Pre-setup No 34) di spec 050. Spec 055 memakai dataset Company Volume yang sama; ukuran gabungan keduanya (48 dan 24 langkah) melebihi sekitar 35 langkah.
- Temuan untuk QA:
  - Pre-setup No 16 mensyaratkan Company khusus dengan akun sendiri; email akun dan nama env var password tidak tertulis (email "disediakan tim FE/BE"), sehingga spec memakai usulan `FA_VOLUME_TC_PASSWORD`.
  - TC-FA-CAID-120 menyebut halaman 2 berisi `Volume Group 110` sampai `Volume Group 101` untuk keyword `Volume Group 1` Descending; ini bergantung pada 21 hasil (`Volume Group 100` sampai `120`) dan ukuran halaman 10. Bila seeding berbeda, asersi halaman 2 ikut berubah.
  - TC-FA-CAID-142 tidak menyebut cara menutup pilihan page size; spec memilih kembali `10`.
