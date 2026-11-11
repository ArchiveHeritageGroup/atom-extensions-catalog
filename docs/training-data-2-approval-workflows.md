---
title: "Training: Data Entry and Workflow, Part 2 - Approval Workflows"
subtitle: "Step-by-step guide to submitting a description for review, claiming tasks from the pool, approving or rejecting each step and reading the workflow history"
author: "Dr Johan Pieterse"
---

| Field | Value |
|---|---|
| Document title | Training: Data Entry and Workflow, Part 2 - Approval Workflows |
| Author | Dr Johan Pieterse |
| Owner | The Archive and Heritage Group (Pty) Ltd |
| Version | 1.0 |
| Status | Released |
| Date | 10 November 2026 |
| Prepared for | Archivists, reviewers and catalogue managers |
| Classification | Public |
| Reference | AHG-TRN-DATA-02 |

: Document control

This guide goes with part 2 of the data entry and workflow training videos. An approval workflow takes a description through a fixed series of steps, such as an initial review and a final approval. Each step is a task that waits in a shared pool until a reviewer claims it, and every decision is kept with the reviewer's comment. Allow about 15 minutes.

## Before you start

| What | Notes |
|---|---|
| Account | An editor, contributor or administrator to submit; a reviewer with the role each step asks for to claim and decide. Workflow administration is for administrators. |
| Plugin | Workflow (ahgWorkflowPlugin), enabled. |
| Version | Plugins v3.121.184 or later. Before v3.121.183 a description could not be submitted for review from its page, and approving or rejecting left an empty error message. |

: What you need before you start

## 1. The workflows

**Workflow administration** (`/workflow/admin`) lists the workflows. The **Standard Review Workflow** is the default for archival descriptions:

| Step | Type | Who |
|---|---|---|
| 1. Initial Review | Review | Any eligible reviewer, from the pool |
| 2. Final Approval | Approve | Any eligible reviewer, from the pool |

: The Standard Review Workflow

Open a workflow to change its name, scope (all records, one repository or one collection) and notifications, and to add, edit or remove steps. A step can be limited to a role or a security clearance, given instructions for the reviewer, and given a number of days before it counts as overdue. The **Collections procedures** workflows cover museum collection procedures such as object entry and loans.

## 2. Submit a description for review

Open the description. The **Workflow** block in the side menu shows **Submit for review**. It opens a confirmation page naming the workflow that applies and its steps. Choose **Submit for review**.

The first step becomes a task waiting in the pool. The Workflow block now shows **In review**, with the current step. The workflow records each decision; it does not change or publish the description.

## 3. Claim a task

Open **Workflow > Task pool** (`/workflow/pool`). It lists the tasks you may take. Choose **Claim task**: the task is assigned to you and leaves the pool. **Release** puts a claimed task back.

## 4. Approve or reject

The task page shows the record, the step's instructions and the history so far. Check the record, enter a comment and choose:

| Decision | Effect |
|---|---|
| Approve | The step is done. The next step becomes a task in the pool, or the workflow completes after the last step. |
| Reject | Needs a comment. The workflow ends as rejected, and the person who submitted the record is notified. After changes, the record can be submitted again. |

: Decisions

**My tasks** lists the tasks you have claimed. The **Workflow dashboard** shows your tasks, the pool, tasks completed today, overdue tasks and recent activity.

When the last step is approved the workflow is complete. Publish the description in the usual way.

## 5. The workflow history

On the record, **Workflow history** lists every event in order: submitted, claimed, approved or rejected, and completed, with the user, the time and the comment.

## Recap

| Step | Where |
|---|---|
| Submit for review | Record, Workflow block |
| Take a task | Workflow, Task pool, Claim task |
| Decide | Task page: comment, Approve or Reject |
| See what happened | Record, Workflow history |

: Recap

Next in this series: part 3, bringing files in - uploads and watched folders.
