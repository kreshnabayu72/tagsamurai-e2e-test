---
id: TC-FA-COA-E2E-019-add-account-klik-backdrop-refresh-sidebar-dan-esc-pada-form-dirty
title: "Add Account: Klik Backdrop, Refresh, Sidebar, dan Esc pada Form Dirty"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-240
  - TC-FA-COA-242
  - TC-FA-COA-243
  - TC-FA-COA-244
  - TC-FA-COA-356
coverage:
  web: automated
---

# Add Account: Klik Backdrop, Refresh, Sidebar, dan Esc pada Form Dirty

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data: nilai `5-6700` hanya diketik dan tidak pernah di-submit, sehingga tidak memakai suffix `{runId}`. Tidak ada akun yang seharusnya tersimpan.
- Kemampuan teknis: mendeteksi dan menolak (memilih tetap di halaman) dialog bawaan browser `beforeunload` saat muat ulang halaman (F5) pada form dirty, serta memastikan dialog itu tidak muncul pada form kosong; disediakan tim FE (S-08).
- Menu sidebar tujuan pada TC-244: salah satu menu sidebar di luar halaman Chart of Accounts; TC tidak menyebut nama menunya, sehingga ditetapkan tim FE (lihat Temuan untuk QA). Menu yang sama dipakai pada kedua kali klik.
- Pembersihan: hook `before` dan `after` spec ini menghapus akun dengan Account Code `5-6700` bila ada; kemampuan hapus lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-240: Klik backdrop saat form dirty

1. Klik `+ Account` di toolbar
2. Ketik `5-6700` di Account Code
3. Klik area backdrop di luar modal
4. Verifikasi modal Add Account tetap terbuka
5. Verifikasi Account Code tetap `5-6700`
6. Verifikasi dialog Unsaved Changes tidak tampil

### TC-FA-COA-356: Tekan `Esc` pada form yang sudah diisi

7. Tekan `Esc`
8. Verifikasi dialog Unsaved Changes tampil dengan teks "You have unsaved changes. Are you sure you want to leave?"
9. Verifikasi dialog memiliki tombol `[Leave]` dan `[Cancel]`
10. Verifikasi modal Add Account tetap terbuka
11. Tekan `Esc` lagi saat dialog Unsaved Changes tampil
12. Verifikasi dialog Unsaved Changes tertutup (setara `[Cancel]`)
13. Verifikasi modal Add Account tetap terbuka
14. Verifikasi Account Code tetap `5-6700`

### TC-FA-COA-242: Refresh halaman saat form dirty

15. Muat ulang halaman (F5)
16. Verifikasi konfirmasi bawaan browser (beforeunload) tampil
17. Pilih tetap di halaman pada konfirmasi bawaan browser
18. Verifikasi modal Add Account dipertahankan
19. Verifikasi Account Code `5-6700` dipertahankan

### TC-FA-COA-244: Klik menu sidebar saat form dirty

20. Klik salah satu menu sidebar di luar halaman Chart of Accounts
21. Verifikasi dialog Unsaved Changes tampil dengan teks "You have unsaved changes. Are you sure you want to leave?"
22. Klik `[Cancel]` pada dialog Unsaved Changes
23. Verifikasi user tetap di halaman Chart of Accounts
24. Verifikasi modal Add Account dipertahankan
25. Verifikasi Account Code `5-6700` dipertahankan
26. Klik menu sidebar yang sama lagi
27. Klik `[Leave]` pada dialog Unsaved Changes
28. Verifikasi user berpindah ke halaman tujuan menu sidebar
29. Buka kembali Fixed Asset > Settings > Accounting > Chart of Accounts
30. Klik `+ Account` di toolbar
31. Verifikasi Account Code kosong (input dibuang)

### TC-FA-COA-243: Refresh halaman saat form belum diisi

32. Muat ulang halaman (F5)
33. Verifikasi tombol `+ Account` di toolbar tampil
34. Verifikasi halaman dimuat ulang tanpa konfirmasi bawaan browser

## Notes

- Spec ini 34 langkah. TC-356 bergantung pada TC-236 (kolom Dependensi) dan TC-244 pada TC-237: langkah "Klik `+ Account`, ketik `5-6700`" milik TC-356 dan TC-244 dipenuhi oleh langkah 1 dan 2 (form dirty yang sama dipakai berurutan oleh TC-240, TC-356, TC-242, dan TC-244). Langkah 3 TC-356 dan langkah 4 TC-356 adalah langkah 7 dan 11.
- Urutan TC di dalam spec berbeda dari penomoran TC (240, 356, 242, 244, 243) agar satu form dirty dipakai berurutan dan TC form kosong (TC-243) berjalan terakhir; alasannya efisiensi pembukaan form (bagian 3, prinsip 6).
- Langkah penghubung (S-03): langkah 29 dan 30 (kembali ke halaman Chart of Accounts dan membuka form baru untuk TC-243; langkah 31 membuktikan input TC-244 dibuang). Form dirty tidak pernah dibiarkan di akhir spec: TC-244 berakhir dengan `[Leave]` (S-08, S-09).
- Absence dialog pada langkah 6 didahului `Verifikasi` modal tetap terbuka (langkah 4); absence konfirmasi bawaan browser pada langkah 34 didahului `Verifikasi` elemen lain pada halaman yang dimuat ulang tampil (langkah 33; 8b butir 2, R-21).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC-244 langkah 3 menyebut "salah satu menu sidebar di luar halaman ini" tanpa nama menu; menu tujuan ditetapkan tim FE.
  - TC-244 Expected (c) "input dibuang" tidak punya langkah observasi di TC; spec mengamatinya dengan membuka kembali form (langkah 29 sampai 31), sebagai langkah tambahan.
  - TC-242 Expected (b) "memilih tetap di halaman" tidak menyebut kontrol dialog bawaan browser; spec memakai kemampuan penolakan dialog `beforeunload` di Prerequisites.
