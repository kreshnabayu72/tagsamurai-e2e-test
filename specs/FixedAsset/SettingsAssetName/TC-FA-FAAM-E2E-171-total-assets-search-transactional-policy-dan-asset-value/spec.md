---
id: TC-FA-FAAM-E2E-171-total-assets-search-transactional-policy-dan-asset-value
title: "Tab Total Assets Search: Kelas Transactional Policy dan Asset Value Commercial"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-802
  - TC-FA-FAAM-809
coverage:
  web: automated
---

# Tab Total Assets Search: Kelas Transactional Policy dan Asset Value Commercial

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Akun berikutnya (ganti akun eksplisit di `## Test Steps`): Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`.
- Akun berikutnya (ganti akun eksplisit di `## Test Steps`): Asset Value HO (Pre-setup #32) `assetValueHO_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_AVHO_PASSWORD`.
- Data: `Column Matrix Item` (Total Asset 6, `AST-2001` sampai `AST-2006`, Pre-setup #33, #33b; policy transaksi Borrow On, Self Service Borrow Off, Assign On, Transfer Off, Pre-setup #33c; Asset Value (Commercial) `AST-2001` 15000000, `AST-2004` 5000000, `AST-2005` 20000000, Pre-setup #33b; `AST-2004` Group `Warehouse` di luar hak `Asset Value HO`, Pre-setup #32). Akun Asset Value HO memegang `View asset value` pada `Head Office` beserta `Finance`; Full Value Access berhak atas seluruh group.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Preferensi Setup Column tersimpan per akun (keputusan pemilik 2026-11-02), jadi centang kolom akun sebelumnya tidak terbawa ke akun berikutnya.
- Kebutuhan NC-25: spec tidak mengasersi bentuk ikon Transactional Policy; hanya hasil pencarian per baris, sesuai keputusan menunggu konfirmasi NC-25.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-802: Search kelas Transactional Policy (nama transaksi pada ikon, terikat visibilitas kolom)

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, centang Transactional Policy, klik `[Save]`
3. Ketik Search `borrow`, tekan Enter
4. Verifikasi keyword `borrow` menampilkan keenam baris (ikon Borrow)
5. Ganti isi kotak search dengan `assign`, tekan Enter
6. Verifikasi keyword `assign` menampilkan keenam baris (ikon Assign)
7. Ganti isi kotak search dengan `transfer`, tekan Enter
8. Verifikasi Title `No results found`
9. Verifikasi Description `Try adjusting your search or filter.`
10. Ganti isi kotak search dengan `self service`, tekan Enter
11. Verifikasi keyword `self service` tidak menemukan baris (policy Off)
12. Klik `(←)` pada kotak Search
13. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang Transactional Policy, klik `[Save]` (sembunyikan kolom)
14. Ketik Search `borrow`, tekan Enter
15. Verifikasi saat Transactional Policy di-hide keyword `borrow` tidak menemukan baris
16. Klik `(←)` pada kotak Search, tutup popup Detail, klik tombol akun, pilih Logout

### TC-FA-FAAM-809: Search kelas Asset Value (Commercial) (nilai pada sel berhak; sel Pending dan No access tidak cocok)

17. Login sebagai Full Value Access (`fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_FVA_PASSWORD`)
18. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
19. Klik header Actions (⋯), pilih `Setup Column...`, centang Asset Value (Commercial), klik `[Save]`
20. Catat teks sel Asset Value `AST-2001` dan `AST-2004` sebagaimana tampil
21. Ketik Search teks nilai `AST-2001` yang dicatat, tekan Enter
22. Verifikasi teks nilai `AST-2001` menampilkan hanya `AST-2001`
23. Ganti isi kotak search dengan teks nilai `AST-2004` yang dicatat, tekan Enter
24. Verifikasi teks nilai `AST-2004` menampilkan hanya `AST-2004`
25. Klik `(←)` pada kotak Search, tutup popup Detail, klik tombol akun, pilih Logout
26. Login sebagai Asset Value HO (`assetValueHO_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_AVHO_PASSWORD`)
27. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
28. Klik header Actions (⋯), pilih `Setup Column...`, centang Asset Value (Commercial), klik `[Save]`
29. Ketik Search teks nilai `AST-2001` yang dicatat, tekan Enter
30. Verifikasi teks nilai `AST-2001` menampilkan `AST-2001`
31. Ganti isi kotak search dengan teks nilai `AST-2004` yang dicatat, tekan Enter
32. Verifikasi teks nilai `AST-2004` tidak menemukan baris karena sel `AST-2004` `No access`
33. Ganti isi kotak search dengan `No access`, tekan Enter
34. Verifikasi Title `No results found`
35. Verifikasi Description `Try adjusting your search or filter.`
36. Ganti isi kotak search dengan `Pending`, tekan Enter
37. Verifikasi Title `No results found` (sel `Pending` `AST-2003` tidak cocok teksnya)
38. Verifikasi Description `Try adjusting your search or filter.`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 802 (Total Control), lalu ganti akun ke Full Value Access dan Asset Value HO untuk 809 (S-07: ganti akun punya langkah eksplisit).
- NC-25 (TC-FA-FAAM-802): ikon final belum dikonfirmasi; asersi hanya pada baris hasil pencarian.
- Langkah penghubung: `(←)` pada Search, menyembunyikan kolom Transactional Policy, menutup popup dan Logout sebelum tiap ganti akun (Login ulang adalah langkah ganti akun eksplisit, S-07).
- Aktor ketiga (Asset Value HO, Pre-setup #32) ada di ACC TC-FA-FAAM-809 ("Aktor: Pre-setup #32e dan Pre-setup #32").
- Temuan untuk QA:
  - TC-FA-FAAM-809 LK langkah 7 ("ulangi langkah 1 sampai 3") tidak menyebut mencentang ulang kolom Asset Value untuk akun kedua; spec mengikuti dengan mengulang langkah centang sebagai bagian pengulangan.
  - TC-FA-FAAM-802 butir c: Expected `transfer` tidak menemukan baris dan alasan policy Off tampil dalam kalimat yang sama; keduanya dipecah menjadi dua Verifikasi.
