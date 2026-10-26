---
id: TC-AC-PP-E2E-024-dialog-publish-confirm-dan-validasi-v01-edit
title: "Validasi V-01 pada Edit dan Dialog Publish Confirm: Screening, Cancel, Esc, Back, dan Klik Luar"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-73
  - TC-AC-PP-74
  - TC-AC-PP-88
coverage:
  web: automated
---

# Validasi V-01 pada Edit dan Dialog Publish Confirm: Screening, Cancel, Esc, Back, dan Klik Luar

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Hook `before` login akun ini dan membuka Settings > Privacy Policy; hook `after` mengembalikan sesi ke akun default suite yang sama (Total Control). Nama env `AC_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active diterbitkan `John Doe` 10 Aug 2026 20:30 UTC dengan H1 `Privacy Policy`, paragraf `This Privacy Policy describes how we collect, use, and protect your information.`, H3 `1. Information We Collect`; Version 2 `John Doe` 02 Jul 2026; Version 1 `Jane Smith` 15 Jan 2026, akun sudah dihapus). Hook `before` men-seed Riwayat A lewat Fixture BE (riwayat versi append-only dan tidak dapat dihapus lewat UI); hook `after` mengembalikan dataset ke Riwayat A. Spec ini tidak pernah menekan `[Publish]` pada Dialog Publish Confirm sehingga tidak membuat versi.
- Dokumen Privacy Policy bersifat tunggal platform-wide; suite berjalan serial (`parallel: false`).
- Riwayat browser: hook `before` membuka halaman lain (mis. halaman awal setelah login) sebelum Settings > Privacy Policy sehingga Browser Back (langkah 36) punya halaman tujuan.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Kemampuan teknis: tombol keyboard Esc; Browser Back; klik pada area gelap di luar dialog; asersi severity tombol (`[Publish]` success, `[Cancel]` Text Contrast).

## Test Steps

### TC-AC-PP-88: Error inline V-01 pada Publish dari state Edit versi Active setelah Clear Field

1. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
2. Tunggu konten editor termuat
3. Klik `[Clear Field]`
4. Klik `[Publish New Version]`
5. Verifikasi error inline "Privacy policy content must not be empty" tampil di bawah editor
6. Verifikasi Dialog Publish Confirm tidak terbuka
7. Ketik "Replacement text." pada editor
8. Verifikasi error inline hilang begitu isi editor berubah
9. Klik `[Clear Field]`
10. Klik `[Publish New Version]`
11. Verifikasi error inline "Privacy policy content must not be empty" muncul lagi
12. Verifikasi Dialog Publish Confirm tidak terbuka
13. Klik `[Clear Field]`
14. Verifikasi error inline hilang setelah `[Clear Field]`

### TC-AC-PP-73: Screening Dialog Publish Confirm saat [Publish New Version] diklik dengan konten valid

15. Ketik " Policy update." di akhir konten
16. Klik `[Publish New Version]`
17. Verifikasi Title dialog "Publish New Privacy Policy Version" (tanpa tanda tanya)
18. Verifikasi body "All users will be required to accept the updated Privacy Policy on their next login. This action cannot be undone. Are you sure you want to publish it?" tanpa bullet nama item
19. Verifikasi footer berisi tombol `[Cancel]` (Text, Contrast) lalu `[Publish]`
20. Verifikasi fokus awal pada `[Cancel]`
21. Verifikasi Modal state Edit tetap terlihat di belakang dialog
22. Verifikasi Modal state Edit di belakang dialog tidak dapat diinteraksi
23. Verifikasi tombol `[Publish]` berseverity success
24. Klik `[Cancel]`

### TC-AC-PP-74: Cancel, Esc, Browser Back, dan klik luar pada Dialog Publish Confirm (idle)

25. Ketik " Cancel path." di akhir konten
26. Klik `[Publish New Version]`
27. Klik `[Cancel]`
28. Verifikasi dialog tertutup
29. Verifikasi kembali ke Modal state Edit
30. Verifikasi " Cancel path." dipertahankan di editor
31. Klik `[Publish New Version]`
32. Tekan Esc
33. Verifikasi dialog tertutup (setara `[Cancel]`)
34. Verifikasi konten editor dipertahankan
35. Klik `[Publish New Version]`
36. Klik Browser Back
37. Verifikasi dialog tertutup (setara `[Cancel]`)
38. Verifikasi halaman tidak berpindah
39. Verifikasi konten editor dipertahankan
40. Klik `[Publish New Version]`
41. Klik area gelap di luar dialog
42. Verifikasi klik luar diabaikan
43. Verifikasi dialog tetap terbuka
44. Klik `[Cancel]`
45. Verifikasi tabel di belakang Modal tidak menampilkan `Version 4`
46. Klik `✕` di header
47. Verifikasi Dialog "Unsaved Changes" tampil
48. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC berubah dari urutan nomor: TC-AC-PP-88 (validasi V-01 yang diblokir) ditaruh pertama mengikuti prinsip 3 konvensi (validasi diblokir sebelum aksi lanjutan). Ketiga TC berbagi satu sesi modal Edit (satu kali buka, satu kali menutup di langkah 46-48) karena tidak ada yang menutup modal.
- TC-AC-PP-73 langkah 1-2 dan TC-AC-PP-74 langkah 1 ("Klik `[⋯]` → Edit") sudah dipenuhi sesi modal TC-AC-PP-88; langkah mengetik " Policy update." (langkah 15) dan " Cancel path." (langkah 25) tetap ditulis sesuai TC. Konten editor pada saat itu dimulai kosong akibat `[Clear Field]` di TC-AC-PP-88, bukan konten Version 3 (TC-AC-PP-73 dan 74 tidak mensyaratkan konten awal).
- Langkah penghubung (tanpa awalan Verifikasi): langkah 24 (`[Cancel]` menutup dialog TC-AC-PP-73), langkah 44 (`[Cancel]` menutup dialog sebelum menutup modal), langkah 46-48 (menutup modal dirty lewat `✕` lalu `[Leave]`, dialog diverifikasi di langkah 47).
- Asersi tambahan yang dicatat: langkah 45 memverifikasi tidak ada `Version 4` di tabel di belakang Modal untuk Expected e TC-AC-PP-74 ("Tidak ada versi baru pada seluruh langkah"); langkah 47 (dialog Unsaved Changes) untuk penutupan deterministik (S-08).
- Jumlah langkah (46) melewati sekitar 35 langkah karena satu `Verifikasi` per klausa Expected (S-01) dan tiga TC satu topik (V-01 dan Dialog Publish Confirm) berbagi satu sesi modal Edit; tiap blok `###` tetap bermakna walau blok sebelumnya gagal (soft assertion) kecuali kegagalan keras membuka modal Edit, sehingga spec tidak dipecah.
- Post Condition TC ("Tidak ada perubahan data", "Tidak ada versi baru dan tidak ada record audit") tanpa langkah observasi tidak diasersi.
- Temuan untuk QA:
  - TC-AC-PP-73 Expected d ("Modal state Edit tetap terlihat di belakang dialog dan tidak dapat diinteraksi") tidak merinci cara menguji "tidak dapat diinteraksi"; spec memverifikasi sebagai pernyataan satu butir tanpa aksi klik tambahan.
  - TC-AC-PP-74 langkah 4 memakai Browser Back saat dialog terbuka tanpa menyatakan ada riwayat browser; spec mengikuti TC dan hanya memverifikasi halaman tidak berpindah.
