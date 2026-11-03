---
id: TC-FA-CF-E2E-092-bulk-sebagian-field-dihapus-aktor-lain-saat-aksi
title: "Bulk Deactivate dan Bulk Delete: Sebagian Field Dihapus Aktor Lain Saat Aksi dan Toast Partial"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-341
  - TC-FA-CF-355
coverage:
  web: automated
---

# Bulk Deactivate dan Bulk Delete: Sebagian Field Dihapus Aktor Lain Saat Aksi dan Toast Partial

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini menonaktifkan dan menghapus field milik sendiri di Company Alpha dan membaca log permanen yang dibagi suite.
- Akun aktor sesi 1 (UI): Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson, Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Akun aktor sesi 2 (API, pelaku kedua yang hanya memicu perubahan state): Total Control sesi 2 (Pre-setup #10, pengguna Rina Putri) `totalControlSecond_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC2_PASSWORD`; memakai sesi API aktor yang tidak dihitung sebagai sesi web (lihat `suite.md`). Password tidak ditulis di spec atau fixture.
- Data baseline Company Alpha (Pre-setup #11 dan #12): delapan field tab General tidak diubah spec ini. Hook `before` memulihkan baseline lewat seed reset Company (disediakan tim FE/BE; fixture baru `Fixture.faCustomFields.baseline`).
- Data Dinamis (di-seed lewat API di hook `before`, bersuffix per run; baseline log nol karena nama unik): `Skip Keep {runId}-092` dan `Skip Gone {runId}-092` (Text, Active; TC-FA-CF-341), `Del Keep {runId}-092` dan `Del Gone {runId}-092` (Text, Active; TC-FA-CF-355). Dengan empat field ini tabel memuat dua belas baris sehingga baris target ditemukan lewat Search. Cleanup: hook `after` menghapus field bersuffix `{runId}-092` yang masih ada lewat API tanpa mengandalkan seeding berhasil penuh.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor sesi 1 dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: penghapusan field oleh sesi API aktor kedua; Search tabel Custom Fields; membaca Modal Changelog, Activity Log (Reports & Logs > Activity Log > Tab User Action), serta System Log `Sarah Johnson` dan `Rina Putri` (Settings > User > Detail pengguna > Tab System Log) dengan kata kunci nama field.
- State global: tidak ada yang diubah selain data field di atas dan flag Guided Tooltip (dipulihkan hook `after`).

## Test Steps

### TC-FA-CF-341: Bulk Deactivate dengan satu field sudah dihapus aktor lain

1. Ketik Search `Skip`, tekan Enter
2. Centang baris `Skip Keep {runId}-092` dan `Skip Gone {runId}-092`
3. Hapus `Skip Gone {runId}-092` lewat sesi API Rina Putri hingga field `Skip Gone {runId}-092` terhapus tersimpan
4. Klik `[Deactivate]` pada Bulk Action Bar
5. Klik `[Deactivate]` pada dialog
6. Verifikasi toast `Success, custom field has been deactivated. Some items were skipped.` tampil
7. Verifikasi switch Active baris `Skip Keep {runId}-092` berada di posisi OFF
8. Verifikasi seleksi di-reset

### TC-FA-CF-355: Bulk Delete dengan satu field sudah dihapus aktor lain

9. Ganti isi kotak search dengan `Del`, tekan Enter
10. Centang baris `Del Keep {runId}-092` dan `Del Gone {runId}-092`
11. Hapus `Del Gone {runId}-092` lewat sesi API Rina Putri hingga field `Del Gone {runId}-092` terhapus tersimpan
12. Klik `[Delete]` pada Bulk Action Bar
13. Klik `[Delete]` pada dialog
14. Verifikasi toast `Success, custom field has been deleted. Some items were skipped.` tampil
15. Verifikasi baris `Del Keep {runId}-092` hilang dari tabel
16. Verifikasi seleksi di-reset

### Pembacaan log untuk TC-FA-CF-341 dan TC-FA-CF-355

17. Klik icon Changelog
18. Ketik Search `{runId}-092` pada Modal Changelog, tekan Enter
19. Verifikasi Modal Changelog memuat satu entri Action `Deactivate` untuk `Skip Keep {runId}-092` dan satu entri Action `Delete` untuk `Skip Gone {runId}-092` dari sesi 2
20. Verifikasi Modal Changelog tidak memuat entri Action `Deactivate` untuk `Skip Gone {runId}-092`
21. Verifikasi Modal Changelog memuat satu entri Action `Delete` untuk `Del Gone {runId}-092` dari sesi 2 dan satu entri Action `Delete` untuk `Del Keep {runId}-092` dari sesi 1
22. Tutup modal Changelog dengan `✕`
23. Buka Activity Log (Reports & Logs > Activity Log > Tab User Action)
24. Cari entri dengan kata kunci `{runId}-092`
25. Verifikasi Activity Log memuat satu entri Action `Deactivate` untuk `Skip Keep {runId}-092` dan satu entri Action `Delete` untuk `Skip Gone {runId}-092` dari sesi 2
26. Verifikasi Activity Log tidak memuat entri Action `Deactivate` untuk `Skip Gone {runId}-092`
27. Verifikasi Activity Log memuat satu entri Action `Delete` untuk `Del Gone {runId}-092` dari sesi 2 dan satu entri Action `Delete` untuk `Del Keep {runId}-092` dari sesi 1
28. Buka System Log `Sarah Johnson` (sesi 1)
29. Cari entri dengan kata kunci `{runId}-092`
30. Verifikasi System Log `Sarah Johnson` memuat satu entri Action `Deactivate` untuk `Skip Keep {runId}-092` dan satu entri Action `Delete` untuk `Del Keep {runId}-092`
31. Verifikasi System Log `Sarah Johnson` tidak memuat entri untuk `Skip Gone {runId}-092` maupun `Del Gone {runId}-092`
32. Buka System Log `Rina Putri` (sesi 2)
33. Cari entri dengan kata kunci `{runId}-092`
34. Verifikasi System Log `Rina Putri` memuat entri Action `Delete` untuk `Skip Gone {runId}-092` dan untuk `Del Gone {runId}-092`

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 341 lalu 355 (keduanya aksi yang mengubah dan menghapus data, paling akhir; S-10); sama dengan urutan TC sumber. Pembacaan keempat surface log dilakukan sekali sesudah kedua TC (langkah 17 sampai 34) dan bukan sesudah tiap TC, karena entri log tiap TC unik per nama field bersuffix `{runId}-092` (baseline nol; S-12) dan tidak saling mengganggu; pemisahan pembacaan per TC menggandakan 18 langkah navigasi dan pembacaan surface yang sama.
- P-1: klausa "tanpa entri Deactivate dari aksi sesi 1" TC-FA-CF-341 dan "field yang dilewati tidak menulis entri dari aksi sesi 1" TC-FA-CF-355 (langkah 20, 26, dan 31) menempel pada state konflik yang dibangun alur ini (satu field terpilih dihapus sesi 2 saat dialog sesi 1 akan dikonfirmasi) dan diasersi pada nama field bersuffix unik `{runId}-092` dengan baseline nol (S-12); tidak ada spec absence yang memuat aksi nyata untuk TC ini (S-05). Anchor positif (8b butir 2): toast partial (langkah 6 dan 14) serta entri Action `Delete` dari sesi 2 untuk `Skip Gone {runId}-092` pada surface yang sama (langkah 19, 25, dan 30 untuk surface Changelog, Activity Log, dan System Log `Sarah Johnson` melalui entri `Skip Keep`/`Del Keep` sesi 1; langkah 34 untuk System Log `Rina Putri`).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 9 (Search agar baris target tampil), langkah 3 dan 11 (pemicu pelaku kedua lewat sesi API), langkah 17, 23, 28, dan 32 (membuka surface log), langkah 18, 24, 29, dan 33 (mencari entri), dan langkah 22 (menutup modal Changelog).
- Asersi tambahan di luar Expected TC (S-03): langkah 7 dan 15 (state akhir field `Skip Keep` dan `Del Keep`, kesimpulan dari "dinonaktifkan" dan "terhapus" TC); langkah 20, 26, dan 31 memecah klausa "tidak ada entri" menjadi `Verifikasi` terpisah dengan anchor positif pada `Verifikasi` presence di surface yang sama (langkah 19, 25, dan 30).
- Data milik spec (S-06, S-12): TC-FA-CF-341 dan TC-FA-CF-355 menyebut field Pre-setup `Asset Serial Tag`, `Legacy Tag`, dan `Compliance File`; spec memakai field Dinamis bersuffix `{runId}-092` agar entri log dapat diasersi dari baseline nol tanpa menghapus field Pre-setup bersama.
- Pelaku kedua (Rina Putri) memakai sesi API karena hanya memicu perubahan state (hapus field); tidak membuka sesi UI kedua dan tidak memakai `P-2`.
- Temuan untuk QA:
  - TC-FA-CF-341 dan TC-FA-CF-355 tidak menyebut kolom atau cara mengenali "dari sesi 2" dan "dari sesi 1" pada Changelog dan Activity Log; spec menyebutkannya sebagai asal aksi (aktor) tanpa menyebut nama kolom.
  - TC-FA-CF-341 dan TC-FA-CF-355 tidak menyebut cara mencari entri pada Activity Log dan System Log; spec memakai kata kunci nama field (mekanisme pencarian mengikuti surface log, belum didefinisikan di TC).
  - TC-FA-CF-355 Expected butir b "field yang dilewati tidak menulis entri dari aksi sesi 1" dan TC-FA-CF-341 Expected butir b "tanpa entri Deactivate dari aksi sesi 1" diasersi lewat langkah 20, 26, dan 31.
  - TC-FA-CF-341 Expected butir b tidak menyebut seleksi di-reset terpisah dari butir c; spec mengikuti butir c (langkah 8).
  - Email akun Total Control sesi 2 (Pre-setup #10) mengikuti pola Pre-setup; env `FA_TC2_PASSWORD` disediakan tim FE.
