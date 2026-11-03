---
id: TC-FA-CF-E2E-144-lisensi-fa7-lapse-tab-accounting-dan-form-aset
title: "Lisensi FA-7 Lapse: Field Accounting Tidak Tampil di Form, Detail, dan Ekspor Aset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-545
  - TC-FA-CF-546
  - TC-FA-CF-654
  - TC-FA-CF-675
coverage:
  web: automated
---

# Lisensi FA-7 Lapse: Field Accounting Tidak Tampil di Form, Detail, dan Ekspor Aset

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company License Lapse (Pre-setup #24). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_LICENSELAPSE_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company License Lapse (Pre-setup #24): field Accounting `Cost Center` Text General Active Required Yes bernilai pada aset `A1`; lisensi FA-7 sudah dicabut dan Grace Period sudah berakhir (T+31 hari); lisensi dapat diaktifkan kembali lewat seed saat sesi berjalan. Nilai data mengacu `Fixture.faCustomFields.licenseLapse` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis: seed Company License Lapse (aktifkan kembali lisensi FA-7 dan pemulihan keadaan lapse; disediakan tim FE/BE); klien HTTP untuk request langsung ke server; fixture BE untuk membaca nilai `Cost Center` aset `A1`; nilai itu dibaca di hook `before` sebagai nilai tersimpan acuan; pengujian berkas unduhan CSV (membuka berkas dan membaca kolom serta baris; disediakan tim FE); penghapusan preferensi Column Visibility Asset List yang disimpan di browser (disediakan tim FE, bagian 4).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: lisensi FA-7 Company License Lapse diaktifkan kembali pada langkah 20. Hook `after` memulihkan keadaan lapse (FA-7 dicabut dan Grace Period berakhir) lewat seed reset Company License Lapse. Hook `after` juga menghapus preferensi Column Visibility Asset List yang disimpan spec di browser pada langkah 22 (bukan `[Reset to Default]`). Suite berjalan serial (`parallel: false`).

## Test Steps

### Keadaan FA-7 dicabut dan Grace Period berakhir (TC-FA-CF-545, TC-FA-CF-654 langkah 1, TC-FA-CF-675 langkah 1 dan 2)

1. Buka form registrasi aset pada modul Asset Registration
2. Verifikasi form registrasi aset tampil
3. Verifikasi field `Cost Center` tidak tampil di form registrasi aset
4. Verifikasi `Cost Center` tidak diwajibkan pada form registrasi aset
5. Buka Detail aset `A1`
6. Verifikasi Detail aset `A1` tampil
7. Verifikasi `Cost Center` tidak tampil di Detail aset `A1`
8. Buka Asset List dan buka daftar Column Visibility
9. Verifikasi daftar kolom opsional memuat sedikitnya satu kolom opsional lain
10. Verifikasi `Cost Center` tidak ada sebagai kolom opsional di Asset List
11. Klik icon Download > `Download as CSV`
12. Verifikasi berkas CSV terunduh
13. Verifikasi berkas CSV tidak memuat kolom `Cost Center`
14. Buka form Edit aset `A1`
15. Verifikasi form Edit aset `A1` tampil
16. Verifikasi `Cost Center` tidak tampil di form Edit aset `A1`
17. Kirim request Edit aset `A1` langsung (klien HTTP) dengan nilai `Cost Center` diubah
18. Verifikasi server merespons 403 Forbidden
19. Verifikasi nilai `Cost Center` aset `A1` tidak berubah (dibaca lewat fixture BE)

### Setelah lisensi FA-7 diaktifkan kembali (TC-FA-CF-654 langkah 2 sampai 4, TC-FA-CF-675 langkah 3, TC-FA-CF-546)

20. Aktifkan kembali lisensi FA-7 Company License Lapse lewat Pre-setup
21. Muat ulang Asset List
22. Tampilkan kolom `Cost Center` lewat Column Visibility
23. Klik icon Download > `Download as CSV`
24. Verifikasi berkas CSV kedua memuat kolom `Cost Center`
25. Verifikasi berkas CSV kedua memuat nilai tersimpan `Cost Center` aset `A1`
26. Muat ulang Settings > Custom Fields lalu klik tab `Accounting`
27. Verifikasi tab `Accounting` dapat dibuka
28. Verifikasi field `Cost Center` tetap Active
29. Verifikasi konfigurasi `Cost Center` tidak berubah (Text, Scope General, Required `Yes`)
30. Buka Detail aset `A1`
31. Verifikasi Detail aset `A1` menampilkan kembali nilai `Cost Center` yang tersimpan
32. Verifikasi nilai `Cost Center` pada Detail aset `A1` tidak berubah dari nilai tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Perubahan urutan TC (S-05, S-10): seluruh asersi keadaan lapse (TC-FA-CF-545, langkah 1 TC-FA-CF-654, langkah 1 dan 2 TC-FA-CF-675) ditaruh sebelum lisensi diaktifkan kembali, dan seluruh asersi keadaan aktif kembali (langkah 2 sampai 4 TC-FA-CF-654, langkah 3 TC-FA-CF-675, TC-FA-CF-546) sesudahnya, supaya aktivasi lisensi dijalankan satu kali.
- P-4: TC-FA-CF-546, TC-FA-CF-654, dan TC-FA-CF-675 berbagi state global yang sama (lisensi FA-7 lapse yang diaktifkan kembali sekali); satu aktivasi di langkah 20 melayani ketiganya dan hook `after` memulihkan keadaan lapse.
- K-1: TC-FA-CF-675 (kelas a) memiliki Expected respons API (403 Forbidden dan state data lewat fixture BE) dan tetap di spec ini; langkah 17 sampai 19 hanya mengasersi status respons dan state data (bagian 8b butir 1).
- Langkah 11 dan 12 TC-FA-CF-654 (Column Visibility tidak menawarkan `Cost Center`) dan Expected b TC-FA-CF-545 diamati dengan satu `Verifikasi` di langkah 10 yang berlaku untuk keduanya.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 20 (aktivasi lisensi lewat seed), langkah 21 (memuat ulang Asset List). Langkah 2, 6, 9, dan 15 adalah anchor positif untuk asersi absence berikutnya (bagian 8b butir 2).
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email akun Total Control Company License Lapse (Pre-setup #24 hanya mendeskripsikan Company); akun disediakan tim FE.
  - Expected a TC-FA-CF-545 menyebut `Cost Center` "tidak diwajibkan" tanpa langkah observasi; langkah 4 menurunkannya dari ketiadaan field di form.
  - Pre-setup #24 tidak menyebut nilai `Cost Center` aset `A1`; spec membandingkan dengan nilai tersimpan yang dibaca lewat fixture BE.
  - Expected b TC-FA-CF-675 dan TC-FA-CF-654 tidak menyebut cara memeriksa "tanpa mengubah data"; spec memakai fixture BE (langkah 19) dan Detail aset (langkah 32).
