---
id: TC-AUTH-OTP-E2E-032-agreement-gate-policy-baru-dan-konfirmasi-sukses
title: "Layar Confirm to Continue: Pemicu Versi Privacy Policy Baru dan Konfirmasi Sukses"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-99
  - TC-AUTH-OTP-103
  - TC-AUTH-OTP-142
coverage:
  web: automated
---

# Layar Confirm to Continue: Pemicu Versi Privacy Policy Baru dan Konfirmasi Sukses

## Prerequisites

- Mode: FE+BE (backend nyata; sesi, persetujuan, dan log dibuktikan lewat perilaku UI dan log Global Settings).
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Password user uji (dipakai TC-AUTH-OTP-142 untuk Login with Password) dari `Spectra.env.OTP_PASSWORD`. Tidak ada password atau token di spec atau fixture.
- Akun aktor hook `before`: Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #11), berhak mempublikasikan versi Privacy Policy di `Admin Console > Settings > Privacy Policy`; password dari `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`. Akun ini dipakai hook `before` untuk menerbitkan versi Privacy Policy, bukan oleh langkah uji.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PP_PASSWORD`, `OTP_PASSWORD`.
- Hook `before` membuka browser admin dan login sebagai akun aktor Total Control (Global Settings); langkah uji hanya berpindah konteks ke browser itu (TC-AUTH-OTP-103). Hook `after` mengembalikan sesi admin ke akun default suite.
- Hook `before`: Principal menerbitkan versi Privacy Policy terbaru sebelum user profil POLICY di-seed. Lalu hook `before` (seeding API) membuat user profil POLICY berikut (Activated, Active ON; sudah login sukses dalam 30 hari terakhir pada device dikenali; persetujuan Privacy Policy versi terbaru belum ada karena Principal (hook `before`) sudah menerbitkan versi yang lebih baru dari versi yang terakhir disetujui user; hanya Agreement terpicu; password `Spectra.env.OTP_PASSWORD`) dengan suffix per run `+{runId}-032`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-99: `Nur Rahmawati` (`nurrahmawati+{runId}-032@qwertysystem.net`)
  - TC-AUTH-OTP-103: `Maya Siregar` (`mayasiregar+{runId}-032@qwertysystem.net`)
  - TC-AUTH-OTP-142: `Fajar Mulyadi` (`fajarmulyadi+{runId}-032@qwertysystem.net`)
- Baseline log: hook `before` mencatat jumlah baris `Maya Siregar` di `Global Settings > Activity Log > Session` dan di `Global Settings > User > Detail > User Log`; "tepat satu baris baru" dan "tidak ada entri log terpisah" pada langkah 24, 26, 27, dan 29 dihitung terhadap baseline itu (S-12).
- Kemampuan teknis: mail-catcher lingkungan uji untuk membaca kode OTP; klien HTTP yang mengirim permintaan Verify OTP langsung ke server tanpa melalui UI dengan email dan kode OTP yang sudah dipakai (TC-AUTH-OTP-99); Principal dengan hak publish Privacy Policy sehingga versi baru diterbitkan di hook `before` sebelum profil POLICY dipakai; dua konteks browser (browser admin dan jendela privat publik); reCAPTCHA mode uji.
- State global: versi Privacy Policy terbaru yang diterbitkan hook `before` tidak ditarik kembali oleh hook `after`; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AUTH-OTP-99: Versi Privacy Policy baru memicu layar Confirm to Continue setelah OTP benar

1. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Ketik `nurrahmawati+{runId}-032@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Ketik 6 digit kode OTP dari email pada kotak digit
6. Verifikasi layar Confirm to Continue tampil dengan Title "Confirm to Continue" (kondisi versi Privacy Policy baru)
7. Buka Portal — Product Hub langsung di tab lain
8. Verifikasi sesi penuh belum dibuat: browser dialihkan ke halaman login
9. Kirim permintaan Verify OTP langsung ke server dengan email `nurrahmawati+{runId}-032@qwertysystem.net` dan kode OTP yang sudah dipakai tadi
10. Verifikasi permintaan Verify OTP dengan kode yang sudah dipakai ditolak server
11. Verifikasi tidak ada sesi yang dibuat

### TC-AUTH-OTP-103: Centang dan Continue pada Agreement tanpa MFA masuk Product Hub

12. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
13. Ketik `mayasiregar+{runId}-032@qwertysystem.net` pada field Email
14. Centang widget reCAPTCHA "I'm not a robot"
15. Klik button [Request OTP]
16. Ketik 6 digit kode OTP dari email pada kotak digit
17. Centang checkbox "I have read and agree to the Privacy Policy *"
18. Klik button [Continue ➔]
19. Verifikasi persetujuan tersimpan
20. Verifikasi browser dialihkan ke Portal — Product Hub
21. Verifikasi sesi aktif untuk `Maya Siregar`
22. Verifikasi halaman MFA tidak tampil
23. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`), buka `Global Settings > Activity Log > Session` dan cari entri untuk `Maya Siregar`
24. Verifikasi tepat satu baris baru dibanding baseline hook `before`: Success `Login with OTP` untuk `Maya Siregar` di `Global Settings > Activity Log > Session`
25. Buka `Global Settings > User > Detail > User Log` untuk `Maya Siregar`
26. Verifikasi tepat satu baris baru dibanding baseline hook `before`: Success `Login with OTP` di `Global Settings > User > Detail > User Log`
27. Verifikasi tidak ada entri log terpisah untuk konfirmasi Agreement di `Global Settings > User > Detail > User Log` selain baris Success `Login with OTP` tersebut
28. Buka kembali `Global Settings > Activity Log > Session` untuk `Maya Siregar`
29. Verifikasi tidak ada entri log terpisah untuk konfirmasi Agreement di `Global Settings > Activity Log > Session` selain baris Success `Login with OTP` pada langkah 24

### TC-AUTH-OTP-142: Persetujuan Privacy Policy dari Login with OTP berlaku pada Login with Password

30. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
31. Ketik `fajarmulyadi+{runId}-032@qwertysystem.net` pada field Email
32. Centang widget reCAPTCHA "I'm not a robot"
33. Klik button [Request OTP]
34. Ketik 6 digit kode OTP dari email pada kotak digit
35. Centang checkbox "I have read and agree to the Privacy Policy *"
36. Klik button [Continue ➔]
37. Logout dari Portal — Product Hub
38. Buka halaman `Auth > Login with Password`
39. Isi Email `fajarmulyadi+{runId}-032@qwertysystem.net` dan Password `Spectra.env.OTP_PASSWORD`, selesaikan reCAPTCHA, lalu klik [Log in]
40. Verifikasi Login with Password berhasil dan browser dialihkan ke Portal — Product Hub
41. Verifikasi sesi aktif untuk `Fajar Mulyadi`
42. Verifikasi layar Confirm to Continue tidak tampil pada Login with Password karena persetujuan versi aktif sudah tersimpan dan kondisi login pertama maupun idle tidak berlaku

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Spec ini memuat tiga TC dengan login penuh masing-masing (42 langkah); tiap TC memakai user dan jendela privat sendiri sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AUTH-OTP-110 (duplikasi tab dengan token pra-autentikasi yang sama) dipindah ke spec multi-konteks `TC-AUTH-OTP-E2E-049-duplikasi-tab-konfirmasi-token-sekali-pakai` (kelas c); spec ini tidak lagi memuat TC-110.
- Pengecualian P-1 (state berat): asersi absence TC-AUTH-OTP-103 (Expected c: "Tidak ada entri log terpisah untuk konfirmasi Agreement") tetap di spec ini (langkah 27 sampai 29) dan tidak dipindah ke spec absence E2E-040, karena bergantung pada state Agreement (layar Confirm to Continue dan persetujuan yang baru dikonfirmasi) di blok ini; TC-AUTH-OTP-132 mencakup kondisi yang sama dari sisi pencatatan. Asersi jumlah ("tepat satu baris Success") bukan absence dan tetap di sini.
- Pengecualian P-2 (pemicu bukan objek uji): langkah 9 memutar ulang kode yang sudah terpakai langsung ke server hanya sebagai langkah observasi Expected c TC-AUTH-OTP-99 dan Post Condition a ("kode OTP berstatus terpakai"), bukan sebagai objek uji replay (kelas a).
- Langkah 30 adalah langkah ganti konteks eksplisit; langkah 37 (logout) adalah langkah dari TC sumber (TC-AUTH-OTP-142) dan langkah 23 adalah ganti konteks ke browser admin (S-03, S-07). Langkah 28 membuka ulang Activity Log Session supaya kedua surface diperiksa untuk Expected c TC-AUTH-OTP-103.
- Temuan untuk QA:
  - TC-AUTH-OTP-99 langkah 6 mengirim Verify OTP langsung dengan kode terpakai saat user berada di layar Confirm to Continue. Penolakan server pada keadaan itu diasumsikan; di PRD baru terbukti untuk kode terpakai setelah login sukses (TC-AUTH-OTP-155). Mohon QA mengonfirmasi bahwa PRD juga menetapkannya pada keadaan Confirm to Continue.
  - TC-AUTH-OTP-142 langkah 9 menyebut "password yang benar" tanpa nilai; spec memakai `Spectra.env.OTP_PASSWORD` yang dipasang saat seeding. Langkah login password tidak menyebut reCAPTCHA maupun tombol; langkah 39 menambah penyelesaian reCAPTCHA dan klik [Log in] yang tidak ada di TC (S-03, S-15), mengikuti login dengan password di modul Login. Label button [Log in] berasal dari halaman Login with Password, bukan dari TC; mohon QA mengonfirmasi.
  - TC-AUTH-OTP-103 Post Condition c menyebut entri Success ditulis sekali dengan detail pada TC Logging; spec memverifikasi jumlah satu baris di kedua surface.
  - TC-AUTH-OTP-103 Expected a dan Post Condition a menyebut "persetujuan tersimpan" tanpa langkah observasi tersendiri; spec mengasersinya hanya sebagai klausa Expected a, yang teramati lewat Continue diterima dan sesi aktif.
