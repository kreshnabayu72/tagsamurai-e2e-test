---
id: TC-AC-LCS-E2E-066-warning-note-client-lifecycle-hilang-dan-tidak-tampil
title: "Warning Note Client Lifecycle: Post-Purge Retention, Nilai Dikembalikan, Save, Muat, dan Reset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-323
  - TC-AC-LCS-324
  - TC-AC-LCS-325
  - TC-AC-LCS-326
coverage:
  web: automated
---

# Warning Note Client Lifecycle: Post-Purge Retention, Nilai Dikembalikan, Save, Muat, dan Reset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); spec menulis nilai uji sesuai TC (S-02).
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Data uji: Post-Purge Retention `730`, Grace Period Duration `30` lalu `20`.
- State global yang diubah: Grace Period Duration tersimpan `20` pada TC-AC-LCS-325, lalu kembali ke default `30` oleh Reset to Default pada TC-AC-LCS-326; pemulihan cadangan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik tab Client Lifecycle

### TC-AC-LCS-323: Mengubah hanya Post-Purge Retention tidak memunculkan warning note

2. Ubah Post-Purge Retention dari `730` menjadi `800`, lalu klik area kosong di luar field (blur)
3. Verifikasi Field Post-Purge Retention tetap tampil bernilai `800`
4. Verifikasi warning note tidak tampil di bawah field Post-Purge Retention
5. Verifikasi `[Save]` enabled
6. Kembalikan Post-Purge Retention menjadi `730`, lalu klik area kosong di luar field (blur)

### TC-AC-LCS-324: Warning note Client Lifecycle hilang saat nilai dikembalikan ke nilai tersimpan

7. Ubah Grace Period Duration dari `30` menjadi `20`, lalu klik area kosong di luar field (blur)
8. Verifikasi warning note tampil di bawah field Post-Purge Retention
9. Kembalikan Grace Period Duration menjadi `30`, lalu klik area kosong di luar field (blur)
10. Verifikasi warning note hilang
11. Verifikasi `[Save]` disabled

### TC-AC-LCS-325: Warning note Client Lifecycle hilang setelah Save berhasil

12. Ubah Grace Period Duration dari `30` menjadi `20`
13. Verifikasi warning note tampil
14. Klik `[Save]`
15. Verifikasi toast sukses "Success, client lifecycle settings have been saved."
16. Verifikasi warning note tidak tampil setelah tab refresh

### TC-AC-LCS-326: Warning note Client Lifecycle tidak tampil saat tab dimuat dan setelah Reset to Default

17. Muat ulang halaman dengan F5, lalu buka tab Client Lifecycle
18. Verifikasi Field Grace Period Duration tampil bernilai `20`
19. Verifikasi warning note tidak tampil
20. Klik `[Reset to Default]`
21. Verifikasi toast sukses "Success, client lifecycle settings have been reset to default."
22. Verifikasi warning note tidak tampil

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (berpindah ke tab Client Lifecycle), langkah 6 (mengembalikan field ke nilai tersimpan, S-09), dan langkah 17 (membuka tab dalam keadaan termuat baru).
- Langkah 3 dan 18 adalah `Verifikasi` anchor field tampil (klausa pertama Expected TC-AC-LCS-323 butir a dan TC-AC-LCS-326 butir a) sebelum asersi absence warning note pada langkah 4 dan 19 (bagian 8b butir 2).
- Langkah 8 adalah asersi tambahan di luar Expected TC-AC-LCS-324 (Expected hanya menyebut warning note hilang); dicatat sebagai anchor positif bagi asersi absence sesudahnya (bagian 8b butir 2).
- Precondition TC-AC-LCS-326 (Grace Period Duration tersimpan `20`) dipenuhi oleh state akhir TC-AC-LCS-325 pada spec yang sama.
- Asersi warning note tidak tampil memakai tab yang sudah termuat (field Post-Purge Retention dan field lain tampil) sebagai anchor permukaan (bagian 8b butir 2).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
  - LK TC-AC-LCS-324 menulis "warning note tampil" pada langkah 1 tanpa butir Expected padanan; spec menambahkan Verifikasinya sebagai anchor (lihat Notes).
  - LK TC-AC-LCS-325 langkah 2 "Amati warning note" dan Expected butir a menyebut warning note tampil tanpa teksnya; spec mengasersi tampilnya saja.
