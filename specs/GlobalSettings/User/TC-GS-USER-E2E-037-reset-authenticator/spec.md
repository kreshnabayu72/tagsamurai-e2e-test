---
id: TC-GS-USER-E2E-037-reset-authenticator
title: Reset Authenticator user lain dan penolakan untuk akun sendiri dan Default User
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-71
  - TC-GS-USER-72
  - TC-GS-USER-94
  - TC-GS-USER-69
  - TC-GS-USER-115
coverage:
  web: automated
---

# Reset Authenticator user lain dan penolakan untuk akun sendiri dan Default User

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), bukan Default User, dengan Authenticator sudah enrolled
- Default User (`totalControlGlobalSettings_automated_qaTeam1`) ada
- User "Rina Wijaya" punya Authenticator enrolled
- User "Tomi Aktif" punya Authenticator enrolled dan akunnya bisa login lewat sesi browser kedua
- Dua sesi browser: sesi pertama untuk aktor (Total Control biasa) dan sesi kedua untuk "Tomi Aktif" yang sedang login dengan sesi MFA aktif
- Reset Authenticator adalah aksi yang butuh flow enrollment MFA ulang. Kebutuhan akun dengan MFA yang bisa dikendalikan skrip disediakan tim FE
- Spec ini mereset Authenticator "Rina Wijaya" dan "Tomi Aktif", jadi keduanya dienroll ulang oleh seeding sebelum run berikutnya

## Test Steps

### Penolakan pada akun sendiri dan Default User

1. Buka User Detail akun aktor sendiri
2. Verifikasi tombol `Reset Authenticator` Disabled dengan tooltip "You can't manage your own account from here."
3. Buka User Detail Default User
4. Verifikasi tombol `Reset Authenticator` Disabled dengan tooltip "Default User cannot be modified."
5. Verifikasi teks tooltip pada langkah 2 dan 4 berbeda satu sama lain

### Reset saat target sedang login

6. Di sesi kedua, pastikan "Tomi Aktif" sedang login dengan sesi MFA aktif
7. Di sesi pertama, buka User Detail "Tomi Aktif" dan klik `Reset Authenticator`
8. Verifikasi dialog "Reset Authenticator" muncul, lalu klik `[Reset]`
9. Verifikasi toast "Success, authenticator has been reset for Tomi Aktif." muncul
10. Di sesi kedua, verifikasi sesi "Tomi Aktif" tidak diputus dan tidak di-logout paksa
11. Di sesi kedua, logout lalu login lagi
12. Verifikasi enrollment MFA baru dipicu pada login berikutnya itu

### Reset user lain

13. Di sesi pertama, buka User Detail "Rina Wijaya" dan klik `Reset Authenticator`
14. Verifikasi dialog "Reset Authenticator" memuat "• Rina Wijaya", "This will remove this user's current authenticator enrollment.", "They will need to set up their authenticator app again the next time multi-factor authentication is required.", dan "Are you sure you want to reset it?", serta tombol `[Cancel]` dan `[Reset]`
15. Klik `[Reset]`
16. Verifikasi toast "Success, authenticator has been reset for Rina Wijaya." muncul
17. Verifikasi status Authenticator "Rina Wijaya" berubah menjadi "Not enrolled yet"
18. Buka Changelog "Rina Wijaya"
19. Verifikasi ada baris Action "Reset Authenticator", Field "Authenticator Enrollment", Old "Enrolled", New "Not Enrolled", dan Modified By admin yang login

## Notes

- Ada tiga varian tooltip Reset Authenticator: Default User, akun sendiri, dan target yang tidak boleh disentuh capability holder. Langkah 5 memastikan varian akun sendiri dan Default User tidak tertukar. Varian target Total Control ditutup `TC-GS-USER-E2E-018-role-negatif-target-terlindungi`.
- Target yang belum enrolled dicakup `TC-GS-USER-E2E-038-reset-authenticator-belum-enrolled`.
- Kegagalan server pada Reset Authenticator (`TC-GS-USER-73`) dicakup spec hanya-FE (`Mode: mock`) yang dibuat kemudian.
- Langkah 6 sampai 12 (sesi login target tidak diputus) ditaruh sebelum reset "Rina Wijaya" hanya karena keduanya tidak saling bergantung.
