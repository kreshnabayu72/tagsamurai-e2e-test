---
id: TC-GS-USER-E2E-043-remove-access-dialog-produk-dengan-aset-atau-approval
title: "Remove Access Produk: Dialog Peringatan Aset atau Approval (Screening, Cancel, Dua Produk, Lanjut Mencabut) dan Tanpa Dialog untuk Produk Tanpa Aset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-218
  - TC-GS-USER-219
  - TC-GS-USER-220
  - TC-GS-USER-221
  - TC-GS-USER-222
  - TC-GS-USER-1008
coverage:
  web: automated
---

# Remove Access Produk: Dialog Peringatan Aset atau Approval (Screening, Cancel, Dua Produk, Lanjut Mencabut) dan Tanpa Dialog untuk Produk Tanpa Aset

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Dinamis (di-seed lewat API di hook `before`, dibersihkan di `after`; menggantikan Joko Susilo No. 19 dan Dewi Lestari No. 12 agar data Pre-setup tidak diubah, S-06):
  - User `Joko Susilo {runId}-043` (email `jokosusilo+{runId}-043@qwertysystem.net`, Activated, Access `Fixed Asset` dan `Supply Asset`) dengan satu borrowed asset dan satu approval in-flight di Fixed Asset serta satu borrowed asset dan satu approval in-flight di Supply Asset. Seeding data Fixed Asset dan Supply Asset (HK8) disediakan tim FE/BE.
  - User `Dewi Lestari {runId}-043` (email `dewilestari+{runId}-043@qwertysystem.net`, Activated, Access `Fixed Asset` dan `Global Settings`) tanpa borrowed asset dan tanpa approval.
- Kemampuan teknis: akun aktor dapat membuka Fixed Asset > Borrow untuk mencari transaksi (client PT Maju Bersama berlangganan Fixed Asset dan Supply Asset, Tabel Data Uji Pre-setup No. 26); baseline jumlah entri Tab Changelog dicatat sebelum aksi pemicu pertama yang diasersi (S-12).
- State global: tidak ada. Spec berjalan serial dengan spec penghapus lain (lihat `suite.md`).
- Cleanup (`after`): hapus kedua user seed beserta borrowed asset, approval, dan transaksi seed (disediakan tim FE/BE).

## Test Steps

### Pembukaan layar

1. Klik icon Search, ketik `Joko Susilo {runId}-043`, tekan Enter
2. Klik Name `Joko Susilo {runId}-043` di User List
3. Klik Tab Changelog
4. Catat jumlah entri Tab Changelog `Joko Susilo {runId}-043` sebagai baseline
5. Klik menu User di sidebar Global Settings
6. Klik icon Search, ketik `Joko Susilo {runId}-043`, tekan Enter

### TC-GS-USER-219 dan TC-GS-USER-1008: Dialog peringatan produk dengan aset atau approval (screening)

7. Klik (⋯) baris `Joko Susilo {runId}-043` → `Edit`
8. Hapus pilihan Access `Fixed Asset`
9. Klik `[Save]`
10. Verifikasi dialog peringatan muncul sebelum submit (belum ada toast sukses)
11. Verifikasi dialog Title `Remove Access`
12. Verifikasi body dialog memuat bullet `• Joko Susilo {runId}-043`
13. Verifikasi body dialog memuat baris dampak `Removing access to Fixed Asset will affect borrowed asset(s) and pending approval(s) — historical data will be preserved, but the user will lose functional access to Fixed Asset.`
14. Verifikasi body dialog diakhiri pertanyaan `Are you sure you want to remove it?`
15. Verifikasi dialog memuat tombol `[Cancel]` dan `[Remove]`

### TC-GS-USER-221: Cancel menahan Popup Edit dengan pilihan Access tetap terhapus

16. Klik `[Cancel]` pada dialog
17. Verifikasi Popup Edit tetap terbuka
18. Verifikasi Access `Fixed Asset` tetap tidak terpilih
19. Klik `✕` pada header Popup Edit
20. Verifikasi dialog `Unsaved Changes`
21. Klik `[Leave]`
22. Verifikasi sel Access baris `Joko Susilo {runId}-043` memuat `Fixed Asset` dan `Supply Asset` (tidak ada perubahan tersimpan)
23. Klik Name `Joko Susilo {runId}-043` di User List
24. Klik Tab Changelog
25. Verifikasi jumlah entri Tab Changelog sama dengan baseline (tidak ada entri Changelog baru)
26. Klik menu User di sidebar Global Settings

### TC-GS-USER-218: Produk tanpa aset atau approval, Save langsung tanpa dialog

27. Klik icon Search, ketik `Dewi Lestari {runId}-043`, tekan Enter
28. Klik (⋯) baris `Dewi Lestari {runId}-043` → `Edit`
29. Hapus pilihan Access `Fixed Asset`
30. Klik `[Save]`
31. Verifikasi toast sukses: "Success, user has been updated."
32. Verifikasi tidak ada dialog peringatan
33. Verifikasi sel Access baris `Dewi Lestari {runId}-043` hanya `Global Settings`

### TC-GS-USER-222: Dua produk terdampak sekaligus, satu dialog gabungan

34. Ganti isi kotak search dengan `Joko Susilo {runId}-043`, tekan Enter
35. Klik (⋯) baris `Joko Susilo {runId}-043` → `Edit`
36. Hapus pilihan Access `Fixed Asset` dan `Supply Asset`
37. Klik `[Save]`
38. Verifikasi hanya satu dialog yang tampil
39. Verifikasi dialog memuat bullet `• Joko Susilo {runId}-043`
40. Verifikasi dialog memuat satu baris dampak untuk Fixed Asset
41. Verifikasi dialog memuat satu baris dampak untuk Supply Asset
42. Verifikasi dialog ditutup pertanyaan yang berakhir `remove them?`

### TC-GS-USER-220: Lanjut mencabut akses dan snapshot historis tetap

43. Klik `[Cancel]` pada dialog
44. Pilih kembali Access `Supply Asset`
45. Klik `[Save]`
46. Klik `[Remove]` pada dialog
47. Verifikasi toast sukses: "Success, user has been updated."
48. Verifikasi sel Access baris `Joko Susilo {runId}-043` memuat `Supply Asset` (pembanding)
49. Verifikasi sel Access baris `Joko Susilo {runId}-043` tanpa `Fixed Asset`
50. Buka Fixed Asset > Borrow, cari transaksi `Joko Susilo {runId}-043`
51. Verifikasi transaksi borrow lama tetap menampilkan nama `Joko Susilo {runId}-043`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Semua TC di spec ini satu topik aksi (Remove Access produk) dan tidak berkelas harness.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (51 langkah) karena enam TC berada di satu topik aksi dan satu layar (Popup Edit dan dialog Remove Access) dengan satu user seed berborrowed asset yang dipakai bersama; tiap blok TC berdiri sendiri. Pembukaan layar dan baseline (langkah 1 sampai 6) tidak dihitung.
- Urutan TC sumber diubah: TC-GS-USER-1008 digabung dengan TC-GS-USER-219 (satu dialog yang sama, satu pembukaan Popup Edit); TC-GS-USER-221 mengikuti dialog itu; TC-GS-USER-222 dan TC-GS-USER-220 berada dalam satu pembukaan Popup Edit (dialog dua produk lalu `[Cancel]`, centang kembali `Supply Asset`, Save, `[Remove]`) karena aksi `[Remove]` pada TC-GS-USER-220 mencabut akses sungguhan dan berada paling akhir (bagian 3 prinsip 5). TC-GS-USER-218 berada sebelum aksi pencabutan Joko Susilo.
- Langkah 44 sampai 46 mengubah keadaan dari dua produk terhapus pilihannya ke hanya `Fixed Asset` terhapus pilihannya, setara langkah TC-GS-USER-220 (hapus pilihan Access `Fixed Asset`, `[Save]`, `[Remove]`).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 sampai 6 (baseline Tab Changelog), 16 (menutup dialog), 19 sampai 21 (menutup Popup Edit dirty, S-08), 23 sampai 24 dan 26 (navigasi ke Tab Changelog dan kembali), 27 dan 34 (Search), 43 (menutup dialog), 44 (pilih kembali).
- Asersi tambahan di luar Expected TC (S-03): langkah 22 (Access tidak berubah) membuktikan "Tidak ada perubahan tersimpan" TC-GS-USER-221; langkah 48 adalah pembanding (anchor) untuk absence `Fixed Asset`; langkah 25 adalah asersi jumlah berbaseline (bukan asersi absence log kelas g).
- Temuan untuk QA:
  - TC-GS-USER-218 Post Condition "Terdampak: Fixed Asset > Settings > User" tidak punya langkah observasi; tidak diasersi (S-01).
  - TC-GS-USER-220 Post Condition "Terdampak: Fixed Asset > Settings > User, approver pool Fixed Asset" tidak punya langkah observasi; tidak diasersi (S-01).
  - TC-GS-USER-222 Expected a tidak memberi teks baris dampak per produk dan Expected b hanya `...remove them?`; spec mengasersi keberadaan satu baris per produk dan akhir pertanyaan.
  - TC-GS-USER-221 langkah 5 menyebut "Buka Tab Changelog Joko Susilo" tanpa menyebut baseline; spec mencatat jumlah entri sebelum aksi dan membandingkannya.
  - TC-GS-USER-1008 duplikat sebagian dengan TC-GS-USER-219 (dialog yang sama); keduanya diasersi dalam satu pembukaan.
  - TC-GS-USER-219, 220, 221, 222 menyebut Joko Susilo Pre-setup (No. 19); spec memakai user seed bersuffix agar data Pre-setup tidak diubah (S-06).
