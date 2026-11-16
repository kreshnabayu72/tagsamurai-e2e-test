---
id: TC-FA-FACO-E2E-088-create-dari-shortcut-dep-preferences
title: "Create Account dari shortcut `+ Create account` pada Select akun Preferences"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FACO-LOGIC-12a, FACO-LOGIC-12b, FACO-LOGIC-12c, FACO-LOGIC-12d, FACO-LOGIC-12e, "§9.5#r6"]
smoke: []
dependsOn: ["Settings > Accounting > Preferences: Select akun dengan shortcut `+ Create account`"]
trace:
  FACO-LOGIC-12a: 10
  FACO-LOGIC-12b: [11, 12]
  FACO-LOGIC-12c: 13
  FACO-LOGIC-12d: [17, 18]
  FACO-LOGIC-12e: [20, 21, 22, 23]
  "§9.5#r6": [11, 12]
anchor: [6]
coverage:
  web: automated
---
# Create Account dari shortcut `+ Create account` pada Select akun Preferences

## Prerequisites
- Aktor: Admin dengan role Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-088-1: Account Code `SCA1-{runId}`, Account Name `Zeta Offset {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, ada di entitas aktor.
  - DU-088-2: Account Code `SCA2-{runId}`, Account Name `Alpha Offset {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, ada di entitas aktor.
  - DU-088-3: Account Code `SCA3-{runId}`, Account Name `Beta Offset New {runId}`, Account Function `Capitalization Offset`, dibuat oleh spec ini lewat shortcut `+ Create account`.
  - Label akun pada Select di Preferences untuk DU-088-3 adalah `SCA3-{runId} – Beta Offset New {runId}`, dari Account Code `SCA3-{runId}` dan Account Name `Beta Offset New {runId}`.
  - DU-088-1 sampai DU-088-3 adalah seluruh akun milik spec ini.

## Test Steps

### Tab Chart of Accounts disiapkan dengan Search, Filter, dan Sort aktif sebelum shortcut dipakai
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon `Filter` di toolbar
3. Pilih Function `Capitalization Offset` pada Filter Panel
4. Klik `[Apply]`
5. Klik header kolom `Account Name`
6. Verifikasi urutan baris dari atas ke bawah `SCA2-{runId}`, `SCA1-{runId}` menurut Account Name dari A ke Z

### Shortcut `+ Create account` pada Select Default Capitalization Offset membuka modal Add Account dengan Account Function terkunci
7. Klik tab `Preferences`
8. Buka Select `Default Capitalization Offset`
9. Klik `+ Create account`
10. Verifikasi modal `Add Account` tampil
11. Verifikasi Account Function pada modal terisi `Capitalization Offset`, sesuai field asal
12. Verifikasi Account Function pada modal Disabled
13. Verifikasi checkbox `Stay on this form after submitting` tidak tampil pada modal

### Submit menutup modal dan akun yang dibuat langsung terpilih di Select Default Capitalization Offset
14. Isi Account Code `SCA3-{runId}`
15. Isi Account Name `Beta Offset New {runId}`
16. Klik `[Submit]`
17. Verifikasi modal `Add Account` tertutup
18. Verifikasi Select `Default Capitalization Offset` langsung menampilkan akun `SCA3-{runId} – Beta Offset New {runId}` sebagai nilai terpilih

### Search, Filter, dan Sort di tab Chart of Accounts tidak di-clear dan akun baru tidak di-highlight
19. Klik tab `Chart of Accounts`
20. Verifikasi kotak Search masih berisi `{runId}`
21. Verifikasi chip filter `Capitalization Offset` masih tampil di atas tabel
22. Verifikasi urutan baris dari atas ke bawah `SCA2-{runId}`, `SCA3-{runId}`, `SCA1-{runId}` menurut Account Name dari A ke Z, bukan urutan default Account Code
23. Verifikasi baris `SCA3-{runId}` tidak di-highlight
