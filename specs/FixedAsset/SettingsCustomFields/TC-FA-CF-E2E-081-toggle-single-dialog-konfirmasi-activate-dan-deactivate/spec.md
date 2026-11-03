---
id: TC-FA-CF-E2E-081-toggle-single-dialog-konfirmasi-activate-dan-deactivate
title: "Toggle Status Single: Dialog Konfirmasi Deactivate dan Activate, Cancel, Esc, dan Konfirmasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-298
  - TC-FA-CF-299
  - TC-FA-CF-300
  - TC-FA-CF-301
  - TC-FA-CF-304
  - TC-FA-CF-305
  - TC-FA-CF-306
coverage:
  web: automated
---

# Toggle Status Single: Dialog Konfirmasi Deactivate dan Activate, Cancel, Esc, dan Konfirmasi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini mengubah status field baseline Company Alpha dan membaca log permanen yang dibagi suite.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson, Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data baseline Company Alpha (Pre-setup #11 dan #12), tab General delapan baris dalam satu halaman: `Asset Serial Tag` (Active, Modified By `Budi S`, Last Updated `17/10/26, 10:45`), `Depreciated Ratio` (Inactive, Modified By `Joko W`, Last Updated `10/10/26, 11:15`), `Storage Capacity`, `Equipment Class`, `Operating Voltage`, `Total Cost`, `Compliance File`, `Legacy Tag`. Hook `before` memulihkan baseline lewat seed reset Company (disediakan tim FE/BE; fixture baru `Fixture.faCustomFields.baseline`). Spec ini mengubah `Asset Serial Tag` dan `Depreciated Ratio` sehingga Last Updated dan Modified By keduanya berubah sampai seed reset berikutnya; hook `after` memulihkan baseline.
- Format tanggal: General Settings Company Alpha `dd/MM/yy` dan 24 jam (Pre-setup #11); jam server dan jam browser sinkron untuk asersi Last Updated (toleransi satu menit).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: membaca jumlah entri Modal Changelog, System Log aktor (Settings > User > Detail pengguna aktor > Tab System Log), dan Activity Log (Reports & Logs > Activity Log > Tab User Action) sebagai baseline (disediakan tim FE/BE; audit trail permanen sehingga total entri tidak diasersi absolut, hanya selisih terhadap baseline); menekan `Esc`.
- State global: tidak ada yang diubah selain status field baseline dan flag Guided Tooltip (dipulihkan hook `after`).

## Test Steps

### Baseline log

1. Catat jumlah entri awal pada Modal Changelog, System Log aktor, dan Activity Log sebagai baseline (aksi baca tanpa `Verifikasi`)

### TC-FA-CF-300: Cancel pada dialog Deactivate single

2. Geser switch Active baris `Asset Serial Tag` ke OFF
3. Klik `[Cancel]`
4. Verifikasi dialog Deactivate tertutup
5. Verifikasi switch Active baris `Asset Serial Tag` kembali ke posisi ON
6. Verifikasi status baris `Asset Serial Tag` tidak berubah: Modified By `Budi S` dan Last Updated `17/10/26, 10:45` tetap
7. Verifikasi tidak ada toast

### TC-FA-CF-306: Cancel pada dialog Activate single

8. Geser switch Active baris `Depreciated Ratio` ke ON
9. Klik `[Cancel]`
10. Verifikasi dialog Activate tertutup
11. Verifikasi switch Active baris `Depreciated Ratio` kembali ke posisi OFF
12. Verifikasi status baris `Depreciated Ratio` tidak berubah: Modified By `Joko W` dan Last Updated `10/10/26, 11:15` tetap
13. Verifikasi tidak ada toast

### TC-FA-CF-301: Esc pada dialog Deactivate setara Cancel

14. Geser switch Active baris `Asset Serial Tag` ke OFF
15. Tekan `Esc`
16. Verifikasi dialog Deactivate tertutup
17. Verifikasi switch Active baris `Asset Serial Tag` kembali ke posisi ON

### Pembacaan log untuk TC-FA-CF-300 dan TC-FA-CF-306

18. Klik icon Changelog
19. Verifikasi jumlah entri Modal Changelog sama dengan baseline langkah 1 (tidak ada entri dari langkah 3 dan 9)
20. Tutup modal Changelog dengan `✕`
21. Buka System Log aktor (Settings > User > Detail pengguna aktor > Tab System Log)
22. Verifikasi jumlah entri System Log aktor sama dengan baseline langkah 1 (tidak ada entri dari langkah 3 dan 9)
23. Buka Activity Log (Reports & Logs > Activity Log > Tab User Action)
24. Verifikasi jumlah entri Activity Log sama dengan baseline langkah 1 (tidak ada entri dari langkah 3 dan 9)

### TC-FA-CF-298 dan TC-FA-CF-299: Dialog Deactivate single dan konfirmasi Deactivate

25. Buka Fixed Asset > Settings > Custom Fields (tab General)
26. Geser switch Active baris `Asset Serial Tag` ke OFF
27. Verifikasi dialog konfirmasi danger berjudul `Deactivate Custom Field` dengan bullet `• Asset Serial Tag`, teks `Deactivating this field will hide it and its data from all asset forms and screens. You can reactivate it later. Are you sure you want to deactivate it?`, serta tombol `[Cancel]` dan `[Deactivate]`
28. Verifikasi switch Active baris `Asset Serial Tag` belum berubah posisi (masih ON) selama dialog tampil
29. Klik `[Deactivate]`
30. Verifikasi dialog tertutup
31. Verifikasi switch Active baris `Asset Serial Tag` berada di posisi OFF
32. Verifikasi toast sukses `Success, custom field has been deactivated.` tampil
33. Verifikasi Last Updated dan Modified By baris `Asset Serial Tag` diperbarui ke waktu aksi (toleransi satu menit) dan aktor `Sarah J`

### TC-FA-CF-304 dan TC-FA-CF-305: Dialog Activate single dan konfirmasi Activate

34. Geser switch Active baris `Depreciated Ratio` ke ON
35. Verifikasi dialog konfirmasi berjudul `Activate Custom Field` dengan bullet `• Depreciated Ratio`, teks `Activating this field will make it and its data visible in all asset forms and screens. Are you sure you want to activate it?`, serta tombol `[Cancel]` dan `[Activate]`
36. Klik `[Activate]`
37. Verifikasi switch Active baris `Depreciated Ratio` berada di posisi ON
38. Verifikasi toast sukses `Success, custom field has been activated.` tampil
39. Verifikasi Last Updated dan Modified By baris `Depreciated Ratio` diperbarui ke waktu aksi (toleransi satu menit) dan aktor `Sarah J`

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (39 langkah). Seluruhnya satu topik (Toggle Status single pada satu Company dan dataset baseline yang sama), dan blok berdiri sendiri: kegagalan satu blok dialog tidak membuat blok lain kehilangan makna; Activate dan Deactivate memakai dialog yang sama sehingga memisahnya hanya menambah login dan hook.
- Urutan TC dalam spec: 300, 306, 301 (tanpa mutasi), pembacaan log, lalu 298 dan 299, 304 dan 305 (aksi yang mengubah data, paling akhir; S-10). Urutan menyimpang dari urutan TC sumber (298, 299, 300, 301, 304, 305, 306) agar baseline log (langkah 1) belum terpengaruh tulisan log dari TC yang mengonfirmasi; dialog TC-FA-CF-298 dan TC-FA-CF-299 dipakai bersama (langkah 26 sampai 29), demikian juga TC-FA-CF-304 dan TC-FA-CF-305 (langkah 34 sampai 36).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (baseline log), langkah 18, 21, dan 23 (membuka surface log), langkah 20 (menutup modal Changelog), dan langkah 25 (kembali ke layar Custom Fields sesudah membaca log). Tabel Alpha delapan baris berada di satu halaman sehingga Search tidak diperlukan untuk menemukan baris target.
- P-1: asersi "tidak ada entri log" TC-FA-CF-300 dan TC-FA-CF-306 (langkah 19, 22, dan 24) berada di spec ini karena bergantung pada state dialog Cancel yang dibangun langkah 2 dan 8 spec ini; dipenuhi dengan baseline jumlah entri (langkah 1; S-12). Dua TC itu dibaca bersama sekali pada langkah 18 sampai 24 karena tidak ada TC yang menulis log di antara langkah 3 dan 24.
- Asersi tambahan di luar Expected TC (S-03): langkah 6 dan 12 menurunkan "status tidak berubah" TC-FA-CF-300 dan TC-FA-CF-306 menjadi Modified By dan Last Updated baseline yang tidak berubah (nilai dari Pre-setup #12 dan TC-FA-CF-635). Langkah 5 dan 11 serta langkah 6 dan 12 dibuat terpisah karena posisi switch dan status tersimpan adalah dua klausa.
- Temuan untuk QA:
  - TC-FA-CF-299 butir c ("Nilai pada aset tidak dihapus, diamati pada TC-FA-CF-313") tidak diasersi di spec ini; diamati di spec 082.
  - TC-FA-CF-300 dan TC-FA-CF-306 mencantumkan Precondition Company Alpha tanpa menyebut akun log yang dibuka; spec memakai System Log akun aktor dan Activity Log sesuai langkah TC. Lokasi menu System Log aktor dan Activity Log diturunkan dari teks Expected TC bagian 5 (Settings > User > Detail pengguna aktor > Tab System Log; Reports & Logs > Activity Log > Tab User Action).
  - Email akun Total Control mengikuti pola Pre-setup `totalControl_automated_{namaCompany}@qwertysystem.net`; penulisan `{namaCompany}` untuk Company Alpha tidak dinyatakan (huruf kecil atau besar).
  - TC-FA-CF-305 butir b ("Last Updated dan Modified By baris diperbarui") dan TC-FA-CF-299 butir b menyebut aktor `Sarah J` hanya di TC-FA-CF-299; spec memakai `Sarah J` untuk keduanya karena akun aktor sama.
