---
id: TC-GS-TAG-E2E-053-delete-konflik-dan-kegagalan-server-single-dan-bulk
title: "Delete: Tag Di-pair Sebelum Commit T-34, Gagal Server T-23/T-24, Sudah Dihapus Admin Lain, dan Klik Ganda"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-TAG-146
  - TC-GS-TAG-147
  - TC-GS-TAG-148
  - TC-GS-TAG-156
  - TC-GS-TAG-330
coverage:
  web: automated
---

# Delete: Tag Di-pair Sebelum Commit T-34, Gagal Server T-23/T-24, Sudah Dihapus Admin Lain, dan Klik Ganda

## Prerequisites

- Mode: FE+BE (backend nyata; kelas b, fault injection lewat intercept di atas backend nyata). Spec ini menghapus data registri pada TC-GS-TAG-330 yang dijalankan terakhir.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua (sesi API aktor, tidak diasersi): Total Control kedua / Admin B (Dewi Lestari) `totalControl2_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC2_PASSWORD`, hanya untuk menghapus DD-02 pada TC-GS-TAG-148. Pemicu pair DD-15 pada TC-GS-TAG-146 memakai sesi API akun FAMS (`famsAdmin_automated_qaTeam1@qwertysystem.net`, `Spectra.env.FA_ADMIN_PASSWORD`; Admin FAMS Hendra Gunawan, Pre-setup TC). Kesamaan akun admin kedua dengan env var terdaftar perlu dikonfirmasi tim FE saat tahap script (Q-2, kategori B).
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30). Baris yang dipakai: DD-02 `E2801160600002054D8A0002` (Available), DD-15 `E28011606000020F00000001` (Available). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec dan sebelum TC-GS-TAG-330 (DD-02).
- Sesi API aktor (kemampuan dinyatakan di `suite.md`): Admin B menghapus DD-02 (langkah 32) dan akun FAMS mem-pair DD-15 (langkah 24).
- Kemampuan teknis (disediakan tim FE/BE): intercept jaringan di atas backend nyata yang memaksa respons 5xx untuk request Delete tag single dan Bulk Delete (endpoint tidak dinamai di TC; ditentukan tahap script dari `openapi.yaml`, S-13), dilepas segera sesudah dipakai (S-09); sesi API pair DD-15 ke aset tepat saat dialog terbuka dan sebelum `Delete` diklik (Q-5, Q-9); sesi API Admin B yang menghapus DD-02 tepat saat dialog terbuka; pembacaan jumlah baris Event Log Tab Activate TAG dan jumlah entri Activity Log (baseline); seed dan reset idempotent Seed Registri A.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): lepas intercept yang tersisa, unpair DD-15, kembalikan Seed Registri A lewat fixture BE, dan kembalikan Rows per page ke 10.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data registri dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-147: Delete single gagal server

1. Aktifkan intercept: request Delete tag single dipaksa gagal 5xx
2. Buka menu baris DD-02, lalu klik `Delete`
3. Klik `Delete` pada dialog
4. Verifikasi toast error `Error, failed to delete TAG.`
5. Verifikasi baris DD-02 tetap di registri
6. Lepas intercept
7. Tutup toast

### TC-GS-TAG-156: Bulk Delete gagal server

8. Klik Tab Not Paired
9. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
10. Aktifkan intercept: request Bulk Delete dipaksa gagal 5xx
11. Centang DD-02 dan DD-15
12. Pilih `Bulk Action` > `Delete`
13. Klik `Delete` pada dialog
14. Verifikasi toast error `Error, failed to delete TAGs.`
15. Verifikasi Bulk Action Bar dipertahankan
16. Verifikasi seleksi dipertahankan
17. Verifikasi daftar di-refresh
18. Lepas intercept
19. Tutup toast
20. Klik `(✕)` pada Bulk Action Bar untuk membatalkan seleksi

### TC-GS-TAG-146: Tag di-pair sebelum commit Delete

21. Klik Tab All
22. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
23. Buka menu baris DD-15, lalu klik `Delete` dan biarkan dialog terbuka
24. Pair tag DD-15 ke aset lewat sesi API akun FAMS hingga tersimpan
25. Klik `Delete` pada dialog
26. Verifikasi toast error `Error, this TAG is currently paired and can't be deleted.`
27. Verifikasi baris DD-15 tetap berstatus `Paired` di registri
28. Tutup toast

### TC-GS-TAG-148: Tag sudah dihapus admin lain

29. Buka Event Log > Tab Activate TAG, catat jumlah baris, lalu tutup modal
30. Buka Global Settings > Activity Log, catat jumlah entri, lalu kembali ke Global Settings > TAG Tab All
31. Buka menu baris DD-02, lalu klik `Delete` dan biarkan dialog terbuka
32. Hapus DD-02 lewat sesi API Admin B hingga tersimpan
33. Klik `Delete` pada dialog
34. Verifikasi toast netral `This TAG is no longer available.`
35. Verifikasi toast itu bukan toast error
36. Verifikasi dialog tertutup
37. Verifikasi daftar di-refresh
38. Verifikasi baris DD-02 tidak ada di registri
39. Buka Event Log > Tab Activate TAG
40. Verifikasi jumlah baris bertambah satu dari nilai yang dicatat (hanya baris Delete milik Admin B, tanpa baris baru dari klik `Delete` ini)
41. Tutup modal Event Log, lalu buka Global Settings > Activity Log
42. Verifikasi jumlah entri bertambah satu dari nilai yang dicatat (hanya entri milik Admin B, tanpa entri baru dari klik `Delete` ini)

### TC-GS-TAG-330: Klik ganda Delete

43. Pulihkan DD-02 menjadi Available lewat fixture BE, buka Global Settings > TAG Tab All, lalu muat ulang halaman
44. Buka Event Log > Tab Activate TAG, catat jumlah baris, lalu tutup modal
45. Buka menu baris DD-02, lalu klik `Delete`
46. Klik dua kali cepat `Delete` pada dialog
47. Verifikasi satu toast sukses `Success, TAG has been deleted.`
48. Verifikasi tidak ada toast error
49. Buka Event Log > Tab Activate TAG
50. Verifikasi satu baris baru Delete (jumlah baris bertambah satu dari nilai yang dicatat)

## Notes

- Mode: FE+BE. Kelas b (fault injection) dan c (konflik dua admin) hadir sebagai pemicu. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (50 langkah nominal). Alasan: seluruh blok adalah penolakan atau kegagalan Delete atas satu dataset (Seed Registri A) dan satu surface (Tab All dan Tab Not Paired); tiap blok berdiri sendiri (intercept dilepas dan data dipulihkan di antara blok), jadi kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pengecualian P-5 butir b: TC-GS-TAG-147 dan TC-GS-TAG-156 adalah dua TC objek-uji ringan kelas b (satu kegagalan 5xx single dan satu kegagalan 5xx bulk) di spec fungsional Delete dengan harness dominan yang sama permukaannya.
- Intercept dilepas segera sesudah pemicu (langkah 6, 18; S-09).
- Pengecualian P-1: asersi bahwa tidak ada entri log baru (langkah 40 dan 42) memakai baseline jumlah entri yang dicatat sebelum dialog dibuka (langkah 29 dan 30), karena state berat (dialog terbuka lalu penghapusan oleh Admin B) dibangun di spec ini; baseline menghitung satu entri milik Admin B.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 7, 19, dan 28 (menutup toast sebelum asersi toast berikutnya, S-09), 8, 20, dan 21 (pindah tab dan membersihkan seleksi), 29, 30, 39, 41, 44, dan 49 (membuka log untuk baseline atau memeriksa hasil), 43 (memulihkan DD-02), 1 dan 10 (mengaktifkan intercept 5xx sebagai pemicu kegagalan), 9 dan 22 (mengubah Rows per page menjadi 50 supaya DD-15 di halaman 2 tampil; dikembalikan ke 10 di hook `after`).
- Perubahan urutan (S-05 butir terakhir): urutan TC sumber (146, 147, 148, 156, 330) disusun ulang menjadi 147, 156, 146, 148, 330. TC-GS-TAG-147 dan 156 memakai DD-02 dan DD-15 saat masih Available; TC-GS-TAG-146 mengubah DD-15 menjadi Paired, TC-GS-TAG-148 menghapus DD-02, sehingga TC-GS-TAG-330 (yang berhasil menghapus DD-02) di akhir setelah DD-02 dipulihkan di langkah 43.
- Asersi tambahan di luar Expected TC (S-03): langkah 35 adalah klausa Expected a TC-GS-TAG-148 ("bukan toast error"), bukan tambahan.
- Temuan untuk QA:
  - Q-5: pemicu pair dan penghapusan "tepat saat dialog terbuka" tidak deterministik dan mekanismenya tidak didefinisikan di TC; disediakan tim FE/BE.
  - TC-GS-TAG-148 Expected b "tidak ada entri log baru" tidak menyebut surface log, sedangkan penghapusan oleh Admin B sendiri menambah satu entri; spec mengasersi selisih satu dari baseline (hanya entri Admin B) di Event Log Tab Activate TAG dan Activity Log.
  - TC-GS-TAG-146 Post Condition tidak ada; TC-GS-TAG-147 dan 148 Expected tidak menyebut apakah dialog tertutup sesudah kegagalan (TC-GS-TAG-147, 156); dialog tidak diasersi pada kedua TC itu.
  - TC-GS-TAG-156 Expected b "daftar di-refresh" tidak menyebut cara mengamati; spec mengasersinya lewat pemuatan ulang data tabel yang dapat diamati harness (disediakan tim FE).
  - TC-GS-TAG-330 "Satu toast sukses dan satu baris Event Log" tidak menyebut teks toast; spec memakai `Success, TAG has been deleted.` (T-21 dari TC-GS-TAG-142).
  - Q-2: akun admin kedua pada Pre-setup TC (`totalControl2_automated_qaTeam1`) dan env var GS_TC2 perlu dikonfirmasi tim FE saat tahap script (Q-2, kategori B).
