---
id: TC-AC-ACC-E2E-145-suspend-unsuspend-dua-tab-idempoten
title: "Suspend dan Unsuspend Race Dua Tab: Aksi Idempoten Tidak Menulis Changelog Baru dan Tidak Mengubah Last Updated"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-196
  - TC-AC-ACC-197
coverage:
  web: automated
---

# Suspend dan Unsuspend Race Dua Tab: Aksi Idempoten Tidak Menulis Changelog Baru dan Tidak Mengubah Last Updated

## Prerequisites

- Mode: FE+BE.
- Konteks (kelas c, dua tab pada satu akun yang diasersi): Tab 1 dan Tab 2 Admin Console > Client dengan sesi akun yang sama.
- Akun aktor: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login di hook `before` spec ini (Tab 1); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data Pre-setup yang diubah lalu dipulihkan lewat UI (S-06): C-08 `PT Mulai Esok` (Active, FAMS Pending; di-Suspend lalu di-Unsuspend) dan C-03 `PT Wahana Nusantara` (Suspended; di-Unsuspend lalu di-Suspend kembali). Efek: baris Changelog `Suspend`/`Unsuspend` dan Last Updated bertambah.
- Kemampuan teknis (jam): jeda 2 menit pada TC dipenuhi dengan memajukan jam server dan jam browser 2 menit (bukan menunggu; konvensi bagian 6), supaya perubahan Last Updated (berketelitian menit) terdeteksi bila aksi idempoten salah menulis. Jam dipulihkan ke waktu nyata segera setelah Last Updated kedua dibaca dan sebelum membaca Changelog; hook `after` memulihkan bila spec berhenti di tengah (S-09).
- Kemampuan teknis (sesi): sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser).
- State global: jam server dan jam browser; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-196: Suspend Client yang sudah Suspended (race dua tab) idempoten

1. Buka Tab 2 Admin Console > Client; pada Tab 1 dan Tab 2 ketik Search `PT Mulai Esok`, tekan Enter
2. [Tab 1] Klik `[Changelog]` di toolbar List, ubah ukuran halaman modal menjadi 100, klik ikon Search, ketik `PT Mulai Esok` lalu tekan Enter, catat jumlah baris Action `Suspend` (N1), lalu tutup modal
3. [Tab 2] Klik `[⋯]` pada baris `PT Mulai Esok` → pilih `Suspend` sampai dialog "Suspend Client" terbuka (jangan klik `[Suspend]`)
4. [Tab 1] Klik `[⋯]` pada baris `PT Mulai Esok` → pilih `Suspend`, lalu klik `[Suspend]` pada dialog
5. [Tab 1] Klik sub-tab Suspended, ketik Search `PT Mulai Esok`, tekan Enter, dan catat nilai kolom Last Updated baris `PT Mulai Esok` (LU1)
6. Majukan jam server dan jam browser 2 menit
7. [Tab 2] Klik `[Suspend]` pada dialog yang sudah terbuka
8. [Tab 2] Verifikasi status `PT Mulai Esok` tetap Suspended tanpa efek ganda
9. [Tab 2] Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tidak tampil
10. [Tab 1] Muat ulang List, klik sub-tab Suspended, ketik Search `PT Mulai Esok`, tekan Enter, dan lihat kolom Last Updated baris `PT Mulai Esok` (LU2)
11. [Tab 1] Verifikasi baris `PT Mulai Esok` tampil di sub-tab Suspended
12. [Tab 1] Verifikasi LU2 sama dengan LU1 (aksi idempoten tidak mengubah Last Updated)
13. Pulihkan jam server dan jam browser ke waktu nyata
14. [Tab 1] Klik `[Changelog]` di toolbar List, ubah ukuran halaman modal menjadi 100, klik ikon Search, ketik `PT Mulai Esok` lalu tekan Enter, dan hitung baris Action `Suspend` (N2)
15. [Tab 1] Verifikasi N2 adalah N1 + 1 (hanya dari langkah 4; aksi idempoten di Tab 2 tidak menulis baris Changelog baru)
16. [Tab 1] Verifikasi baris teratas (Date terbaru, bertanggal hari ini): Action `Suspend`, Client Name `PT Mulai Esok`, Field `Status`, Old Value `Active`, New Value `Suspended`
17. [Tab 1] Tutup modal Changelog, lalu pada baris `PT Mulai Esok` klik `[⋯]` → pilih `Unsuspend` dan klik `[Unsuspend]` pada dialog
18. Tutup Tab 2

### TC-AC-ACC-197: Unsuspend Client yang sudah Active (race dua tab) idempoten

19. Buka Tab 2 Admin Console > Client, klik sub-tab Suspended pada Tab 1 dan Tab 2; pada kedua tab ketik Search `PT Wahana Nusantara`, tekan Enter
20. [Tab 1] Klik `[Changelog]` di toolbar List, ubah ukuran halaman modal menjadi 100, klik ikon Search, ketik `PT Wahana Nusantara` lalu tekan Enter, catat jumlah baris Action `Unsuspend` (N1), lalu tutup modal
21. [Tab 2] Klik `[⋯]` pada baris `PT Wahana Nusantara` → pilih `Unsuspend` sampai dialog "Unsuspend Client" terbuka (jangan klik `[Unsuspend]`)
22. [Tab 1] Klik `[⋯]` pada baris `PT Wahana Nusantara` → pilih `Unsuspend`, lalu klik `[Unsuspend]` pada dialog
23. [Tab 1] Klik sub-tab Active, ketik Search `PT Wahana Nusantara`, tekan Enter, dan catat nilai kolom Last Updated baris `PT Wahana Nusantara` (LU1)
24. Majukan jam server dan jam browser 2 menit
25. [Tab 2] Klik `[Unsuspend]` pada dialog yang sudah terbuka
26. [Tab 2] Verifikasi status `PT Wahana Nusantara` tetap Active tanpa efek ganda
27. [Tab 1] Muat ulang List, klik sub-tab Active, ketik Search `PT Wahana Nusantara`, tekan Enter, dan lihat kolom Last Updated baris `PT Wahana Nusantara` (LU2)
28. [Tab 1] Verifikasi baris `PT Wahana Nusantara` tampil di sub-tab Active
29. [Tab 1] Verifikasi LU2 sama dengan LU1 (aksi idempoten tidak mengubah Last Updated)
30. Pulihkan jam server dan jam browser ke waktu nyata
31. [Tab 1] Klik `[Changelog]` di toolbar List, ubah ukuran halaman modal menjadi 100, klik ikon Search, ketik `PT Wahana Nusantara` lalu tekan Enter, dan hitung baris Action `Unsuspend` (N2)
32. [Tab 1] Verifikasi N2 adalah N1 + 1 (hanya dari langkah 22; aksi idempoten di Tab 2 tidak menulis baris Changelog baru)
33. [Tab 1] Verifikasi baris teratas (Date terbaru, bertanggal hari ini): Action `Unsuspend`, Client Name `PT Wahana Nusantara`, Field `Status`, Old Value `Suspended`, New Value `Active`
34. [Tab 1] Tutup modal Changelog, lalu pada baris `PT Wahana Nusantara` klik `[⋯]` → pilih `Suspend` dan klik `[Suspend]` pada dialog
35. Tutup Tab 2

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Awalan `[Tab 1]` dan `[Tab 2]` menandai konteks.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) dan baseline Changelog (S-12) atas dua TC satu jenis harness (dua tab dan pengaturan jam); tiap blok memakai Client sendiri dan memulihkan statusnya sehingga tetap bermakna walau blok sebelumnya gagal.
- Jeda "Tunggu 2 menit" pada TC dipenuhi dengan memajukan jam (langkah 6 dan 24), bukan menunggu (R-10). Jam dipulihkan sebelum membaca Changelog (langkah 13 dan 30; S-09, S-12): log yang dibuat saat jam digeser tidak ada di sini karena Tab 2 idempoten, dan asersi memakai selisih jumlah baris terhadap baseline N1.
- Langkah penghubung (tanpa awalan Verifikasi): membuka dan menutup Tab 2 (langkah 1, 18, 19, 35), pemulihan status (langkah 17 dan 34; Post Condition TC), penutupan modal Changelog, dan Search yang menemukan baris target (R-16).
- Post Condition TC-AC-ACC-196 dan 197 adalah aksi pemulihan dan sudah menjadi langkah.
- Temuan untuk QA:
  - TC-AC-ACC-196 dan 197 Expected a ("Tab 2 tidak menerapkan efek ganda") tidak menyebut keadaan yang diamati di Tab 2 selain status tetap; spec mengasersi baris/status yang tampil setelah aksi di Tab 2.
