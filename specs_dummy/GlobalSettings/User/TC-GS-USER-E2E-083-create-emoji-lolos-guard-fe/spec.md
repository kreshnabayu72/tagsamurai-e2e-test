---
id: TC-GS-USER-E2E-083-create-emoji-lolos-guard-fe
title: 'Create menolak emoji yang lolos guard FE lewat manipulasi DOM'
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-193
coverage:
  web: automated
---

# Create menolak emoji yang lolos guard FE lewat manipulasi DOM

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Kemampuan menyuntikkan nilai ke input lewat manipulasi DOM (bukan mengetik) disediakan skrip
- Position dan Division valid ada di master data

## Test Steps

1. Klik `[+ User]` dan isi semua field wajib dengan data valid
2. Sisipkan emoji ke input Full Name lewat manipulasi DOM (bukan mengetik) sehingga guard keystroke dilewati
3. Klik `[Submit]`
4. Verifikasi user tidak dibuat
5. Verifikasi ada penolakan dengan pesan "Full Name contains invalid characters" atau setara dari validasi server, dan tidak ada toast sukses

## Notes

- Sumber `user.md` bagian 4.4 dan `foundation/process/prd-process/prd-conventions.md` (fallback "[Field] contains invalid characters" bila block-di-input gagal).
- Layer 1 (emoji tidak bisa diketik) dicakup spec validasi form Create. Ini layer 2: pertahanan lapis kedua di server.
- Nama field pada pesan mengikuti label field yang terisi emoji. TC sumber menulis "Name".
