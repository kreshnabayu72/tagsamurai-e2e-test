---
id: TC-GS-USER-E2E-154-pagination-input-nomor-halaman
title: Input nomor halaman di pagination langsung membuka halaman itu
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-613
coverage:
  web: automated
---

# Input nomor halaman di pagination langsung membuka halaman itu

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Minimal 101 login user, page size 10
- Spec ini hanya membaca data

## Test Steps

1. Buka sub-tab "Login User" di User List
2. Ketik 5 di input nomor halaman
3. Tekan Enter
4. Verifikasi tabel pindah ke halaman 5 dan indikator halaman menunjukkan 5
5. Ketik nomor di luar rentang (mis. 999) lalu Enter dan verifikasi tabel tetap di halaman yang valid tanpa error

## Notes

- Sumber `user.md` §4.3 dan §5 ("input nomor halaman langsung").
- Perilaku nomor di luar rentang tidak didefinisikan PRD; spec hanya memverifikasi tidak ada error.
