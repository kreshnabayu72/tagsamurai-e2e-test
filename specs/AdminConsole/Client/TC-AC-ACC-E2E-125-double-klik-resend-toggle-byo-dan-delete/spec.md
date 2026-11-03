---
id: TC-AC-ACC-E2E-125-double-klik-resend-toggle-byo-dan-delete
title: "Double-klik Resend Activation Email, [Enable] Toggle BYO, dan [Delete] Hanya Memproses Satu Kali"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-666
  - TC-AC-ACC-660
  - TC-AC-ACC-659
coverage:
  web: automated
---

# Double-klik Resend Activation Email, [Enable] Toggle BYO, dan [Delete] Hanya Memproses Satu Kali

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data Pre-setup: C-02 `PT Teknologi Maju` (Default User Not Yet Activated, FAMS Grace; Resend hanya menambah baris Changelog dan mengirim email, tidak ada perubahan state yang perlu dipulihkan); C-01 `PT Sejahtera Abadi` (toggle BYO awal Disabled; diubah ke Enabled lalu dipulihkan ke Disabled; efek: baris Changelog `Edit` dan Last Updated bertambah); C-LIF-24 `PT Uji Konkurensi 06` (Tabel A3, kelas Dikonsumsi: dihapus oleh blok TC-AC-ACC-659; di-seed ulang tanpa syarat oleh Fixture BE yang disediakan tim FE/BE di hook `before` dan `after`).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client dan Detail disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-666: Double-klik [Resend Activation Email] hanya memproses satu kali

1. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Teknologi Maju` lalu tekan Enter
2. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Resend Activation Email` untuk "PT Teknologi Maju" (N0), lalu tutup modal
3. Ketik Search `PT Teknologi Maju`, tekan Enter, klik Company Name `PT Teknologi Maju`
4. Klik `[Resend Activation Email]` dua kali cepat
5. Verifikasi `[Resend Activation Email]` ter-disable segera setelah klik pertama
6. Verifikasi toast "Success, activation email has been sent." tampil satu kali
7. Tunggu aksi selesai (tombol `[Resend Activation Email]` aktif kembali)
8. Klik breadcrumb "Client" lalu klik `[Changelog]` di toolbar, klik ikon Search di modal Changelog, ketik `PT Teknologi Maju` lalu tekan Enter, ubah ukuran halaman modal menjadi 100
9. Verifikasi jumlah baris Action `Resend Activation Email` untuk "PT Teknologi Maju" adalah N0 + 1
10. Verifikasi baris baru: Action `Resend Activation Email`, Client Name "PT Teknologi Maju", Field `Email`
11. Tutup modal Changelog

### TC-AC-ACC-660: Double-klik [Enable] pada dialog toggle BYO Activation Setting hanya memproses satu kali

12. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Sejahtera Abadi` lalu tekan Enter
13. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Edit` Field `Allow Self-Purchased Device Activation` untuk "PT Sejahtera Abadi" (N0), lalu tutup modal
14. Ketik Search `PT Sejahtera Abadi`, tekan Enter, klik Company Name `PT Sejahtera Abadi`
15. Geser toggle "Allow Self-Purchased Device Activation" ke Enabled
16. Tunggu toast lama hilang
17. Klik `[Enable]` dua kali cepat
18. Verifikasi `[Enable]` ter-disable segera setelah klik pertama
19. Verifikasi toast "Success, self-purchased device activation setting has been updated." tampil satu kali
20. Verifikasi toggle berstatus Enabled
21. Klik breadcrumb "Client" lalu klik `[Changelog]` di toolbar, klik ikon Search di modal Changelog, ketik `PT Sejahtera Abadi` lalu tekan Enter, ubah ukuran halaman modal menjadi 100
22. Verifikasi jumlah baris Action `Edit` Field `Allow Self-Purchased Device Activation` adalah N0 + 1
23. Verifikasi baris baru: Action `Edit`, Field `Allow Self-Purchased Device Activation`, Old Value `Disabled`, New Value `Enabled`
24. Tutup modal Changelog, buka kembali Detail `PT Sejahtera Abadi`
25. Geser toggle ke Disabled

### TC-AC-ACC-659: Double-klik [Delete] pada dialog Delete hanya memproses satu kali

26. Klik breadcrumb "Client", klik `[Changelog]` di toolbar, klik ikon Search di modal Changelog, ketik `PT Uji Konkurensi 06` lalu tekan Enter
27. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Delete` untuk "PT Uji Konkurensi 06" (N0), lalu tutup modal
28. Ketik Search `PT Uji Konkurensi 06`, tekan Enter
29. Klik `[⋯]` pada baris `PT Uji Konkurensi 06` → pilih `Delete`
30. Ketik nama persis `PT Uji Konkurensi 06` pada input "Type the client name to confirm" dan centang "I understand this action cannot be undone"
31. Tunggu toast lama hilang
32. Klik `[Delete]` dua kali cepat
33. Verifikasi `[Delete]` ter-disable segera setelah klik pertama
34. Verifikasi toast "Success, client has been deleted." tampil satu kali
35. Verifikasi tidak ada toast error
36. Verifikasi baris `PT Uji Konkurensi 06` tidak tampil di sub-tab Active
37. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Uji Konkurensi 06` lalu tekan Enter, ubah ukuran halaman modal menjadi 100
38. Verifikasi jumlah baris Action `Delete` untuk "PT Uji Konkurensi 06" adalah N0 + 1
39. Verifikasi baris baru: Action `Delete`, Field `Company Name`, Old Value `PT Uji Konkurensi 06`, New Value `—`
40. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) dan baseline Changelog (S-12) atas tiga TC satu topik (guard double-klik pada tombol konfirmasi aksi Detail dan Delete), satu akun, satu kelas harness; tiap blok memakai Client sendiri sehingga tetap bermakna walau blok sebelumnya gagal. Aksi yang menghabisi data (Delete) ditaruh paling akhir (prinsip 5).
- Langkah penghubung (tanpa awalan Verifikasi): "Tunggu aksi selesai" sesudah Resend (langkah 7), "Tunggu toast lama hilang" sebelum asersi hitungan toast (langkah 16 dan 31; R-12), pemulihan toggle ke Disabled (langkah 25; Post Condition TC-AC-ACC-660), penutupan modal Changelog, dan Search yang menemukan baris target. Asersi absence baris `PT Uji Konkurensi 06` (langkah 36) berlandaskan toast sukses Delete yang sudah diasersi sebagai anchor (butir 2 bagian 8b).
- Post Condition TC-AC-ACC-666: `-`; TC-AC-ACC-659 ("Seed ulang C-LIF-24") dilakukan di hook.
- Temuan untuk QA:
  - TC-AC-ACC-666 Expected c menyebut "Field `Email`" tanpa Old Value dan New Value; spec mengasersi kolom yang disebut TC.
