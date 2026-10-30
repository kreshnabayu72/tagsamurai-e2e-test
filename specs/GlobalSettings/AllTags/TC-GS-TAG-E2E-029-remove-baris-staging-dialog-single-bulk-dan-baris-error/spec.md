---
id: TC-GS-TAG-E2E-029-remove-baris-staging-dialog-single-bulk-dan-baris-error
title: "Remove Baris Staging: Dialog Single, Bulk Remove Jamak, Collapse ke Single, dan Baris Error Tidak Memblokir Submit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-89
  - TC-GS-TAG-91
  - TC-GS-TAG-92
  - TC-GS-TAG-94
coverage:
  web: automated
---

# Remove Baris Staging: Dialog Single, Bulk Remove Jamak, Collapse ke Single, dan Baris Error Tidak Memblokir Submit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun (dua client; akun pertama di hook `before`, ganti akun eksplisit di langkah 34):
  - Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi), `Spectra.env.GS_TC_PASSWORD`.
  - Total Control Client NoByo `totalControl_automated_qaNoByo@qwertysystem.net` (Eka Pratama), `Spectra.env.GS_TC_NOBYO_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`, lihat `suite.md` bagian Kredensial); opsi mandiri nonaktif; stok resmi Client NoByo memuat IMEI `356938035643001` Available (seeding disediakan tim FE/BE).
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Stok resmi Admin Console Client A (Device Name `Teltonika FMB920`, SKU `SKU-GPS-01`, Brand `Teltonika`, Model/Type `FMB920`) di-seed idempotent oleh fixture BE di hook `before`: GPS `356938035643001` (DD-S1) Available, `356938035643002` (DD-S2) Damaged/Missing, dan `356938035643003` (DD-S3) Available. Akun Admin Console untuk seeding stok disediakan tim FE (S-13).
- Data identifier: `356938035643101` (DD-N1) tidak ada di stok resmi Client NoByo (Error saat opsi mandiri nonaktif).
- Kemampuan teknis: entri manual GPS (input teks dan tombol `Add`; label dan placeholder kontrol menunggu desain, NC-11, selektor disediakan tim FE sesuai plan bagian 6) dan unggah berkas CSV/XLSX; tidak ada endpoint atau selektor yang dikarang spec ini.
- Spec tidak melakukan Submit Activation (TC-94 menutup dialog `Submit Activation` tanpa mengonfirmasi); registri kedua client tidak berubah. Aksi Remove (destruktif atas staging) ditaruh di akhir bagian Client A (prinsip 5 bagian 3).
- Suite serial (`parallel: false`); spec tidak bergantung pada hasil spec lain. Identifier TAG (EPC, IMEI, UID) tetap dan tidak dapat diberi sufiks `{runId}` (S-12), sehingga seeding bersifat idempotent: hook `before` mengembalikan data yang dipakai spec ini ke kondisi awal (Q-4).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya; lihat `suite.md` bagian Hook Guided Tooltip.
- Nilai data mengacu ke `fixtures/all-tags.json` (identitas saja, dibuat tahap script); tidak ada password di fixture.

## Test Steps

### Client A

1. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
2. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643001`

### TC-GS-TAG-89: Remove baris lewat row action memakai Dialog 12 single

3. Klik `Remove` pada baris `356938035643001`
4. Verifikasi dialog `Remove TAG` dengan bullet `356938035643001`
5. Verifikasi dialog memuat baris `Are you sure you want to remove it?`
6. Verifikasi tombol dialog `Cancel` dan `Remove` (danger)
7. Verifikasi baris `Removing by scan is more accurate...` tidak tampil untuk GPS
8. Klik `Cancel`
9. Verifikasi dialog tertutup
10. Verifikasi baris `356938035643001` tetap di staging

### TC-GS-TAG-92: Bulk Remove dengan satu baris collapse ke dialog single

11. Centang baris `356938035643001`
12. Pilih `Bulk Action` > `Remove`
13. Verifikasi dialog berjudul `Remove TAG` (singular)
14. Verifikasi dialog memuat satu bullet `356938035643001`
15. Verifikasi dialog memuat baris `Are you sure you want to remove it?`
16. Klik `Cancel` pada dialog
17. Hapus centang baris `356938035643001`

### TC-GS-TAG-91: Bulk Remove dua baris atau lebih

18. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643002` lalu `356938035643003`
19. Centang ketiga baris `356938035643001`, `356938035643002`, `356938035643003`
20. Pilih `Bulk Action` > `Remove`
21. Verifikasi dialog berjudul `Remove TAGs` (jamak)
22. Verifikasi dialog memuat tiga bullet kode `356938035643001`, `356938035643002`, `356938035643003`
23. Verifikasi dialog memuat baris `Are you sure you want to remove them?`
24. Verifikasi tombol dialog `Cancel` dan `Remove`
25. Klik `Remove`
26. Verifikasi `Total Scanned: 0`
27. Verifikasi tiga baris hilang dari staging

### TC-GS-TAG-89 (lanjutan): Remove single dikonfirmasi

28. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643001`
29. Klik `Remove` pada baris `356938035643001`, lalu klik `Remove` pada dialog
30. Verifikasi `Total Scanned: 0`
31. Verifikasi baris `356938035643001` hilang dari staging
32. Kembali ke List: klik item sidebar `TAG` (staging kosong)

### Client NoByo

33. Ganti akun: logout, login sebagai Total Control Client NoByo (`Spectra.env.GS_TC_NOBYO_PASSWORD`)
34. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`

### TC-GS-TAG-94: Baris Error dapat dihapus dan tidak memblokir Submit

35. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101` (tidak di stok) dan `356938035643001` (Official)
36. Verifikasi baris `356938035643101` berstatus `Error`
37. Klik `Submit`
38. Verifikasi dialog `Submit Activation` muncul (Submit tidak diblokir)
39. Verifikasi dialog `Submit Activation` memuat hanya `356938035643001`
40. Verifikasi baris `Error` `356938035643101` tidak tercantum di dialog (dikecualikan dari commit)
41. Tutup dialog `Submit Activation` tanpa mengonfirmasi
42. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Kelas harness: fungsional (Remove pada staging GPS).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Alasan di atas sekitar 35 langkah: satu kelas harness (staging GPS), blok TC berdiri sendiri; ganti akun eksplisit (langkah 34) sah (pemisah akun kasus b) karena bagian sesudah ganti akun tetap bermakna walau bagian Client A gagal; total 43 langkah, sedikit di atas batas karena prefix mulai sesi dan penambahan entri berulang.
- Urutan: Dialog Cancel (TC-89, TC-92) dan Bulk Remove (TC-91) lebih dulu, lalu konfirmasi Remove single (TC-89 lanjutan) di akhir bagian Client A karena menghapus baris staging (prinsip 5 bagian 3). Remove single pada TC-89 langkah 8 dipisah sebagai blok `lanjutan` setelah TC-91 sehingga baris `356938035643001` tersedia untuk TC-92 dan TC-91; baris `356938035643001` ditambahkan lagi pada blok lanjutan.
- Langkah penghubung (tanpa `Verifikasi`): langkah mulai sesi menggabungkan TC langkah 1 sampai 3; `Klik Cancel pada dialog` dan `Hapus centang` pada TC-92 menjaga state antar TC (S-09); `Tutup dialog Submit Activation` pada TC-94 menghindari commit; `Verifikasi baris ... berstatus Error` pada TC-94 adalah anchor positif (butir 2 bagian 8b) untuk asersi dialog; `Kembali ke List` dengan `Leave` adalah langkah penghubung (S-03): sesi dengan baris staging dianggap dirty sehingga keluar halaman memunculkan dialog konfirmasi; definisi dirty dan teks dialog diuji di spec 036 (TC-183 sampai TC-185, TC-111 sampai TC-113) dan tidak diasersi di spec ini (`Leave` tanpa `Verifikasi` dialog).
- Rujukan: pencocokan dan lencana `Error` pada baris staging ada di spec 022, 023, dan 025; commit Submit Activation (dialog `Submit Activation` lengkap dan toast) ada di spec 031.
- Temuan untuk QA:
  - TC-94 Langkah 5 dan 6 mengamati dialog `Submit Activation` tanpa menyebut tombol penutup/konfirmasi; spec menutup dialog tanpa konfirmasi dan tanpa menulis label tombol (label diuji di spec 031).
  - TC-94 Expected b ("Baris Error dikecualikan dari commit") diasersi lewat isi dialog `Submit Activation`; hasil commit tidak diamati (spec tidak melakukan Submit).
  - TC-91 Skenario menyebut "bullet list scrollable" tetapi Expected tidak memuat asersi scroll; spec tidak mengasersinya.
  - TC-89 Expected b ("Baris `Removing by scan...` tidak tampil untuk GPS") adalah klaim absence; anchor positif adalah dialog `Remove TAG` yang diverifikasi pada langkah yang sama.
